import re
import sqlite3
from database import DATABASE_NAME

def normalize_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return " ".join(text.split())

def get_legal_guidance(user_issue):
    issue = normalize_text(user_issue)
    if not issue:
        return []

    synonyms = {
        "maintenance": [
            "financial support", "living expenses", "husband left me",
            "refuses to provide money", "support our child", 
            "child support", "abandoned me"
        ],
        "sexual harassment": [
            "inappropriate touching", "touching me", "sexual messages",
            "unwanted advances", "boss harassing", "inappropriate messages"
        ],
        "domestic violence": [
            "husband hits", "beats me", "physical abuse", "abusive husband",
            "violence at home", "in laws threaten", "domestic abuse"
        ],
        "dowry harassment": [
            "demand money", "money from my parents", "in laws demand",
            "dowry demand", "harassment by in laws"
        ],
        "stalking": [
            "following me", "follows me", "keeps calling", "tracking me",
            "unwanted calls", "waiting outside", "multiple messages"
        ],
        "inheritance": [
            "property share", "father passed away", "inherit property",
            "brother refuses property", "ancestral property", 
            "father's property", "family property", "inheritance denied",
            "share of the property", "daughter property rights"
        ],
        "unequal remuneration": [
            "lower salary", "paid less", "pay discrimination", 
            "unequal salary", "same work", "gender pay gap"
        ],
        "economic abuse": [
            "controls my bank account", "takes my salary", "financial control",
            "refuses to give money", "denied access to money", 
            "controls my salary", "controls my finances"
        ]
    }

    def phrase_matches(phrase):
        phrase = normalize_text(phrase)
        if not phrase:
            return False

        pattern = r"\b" + re.escape(phrase) + r"\b"
        return re.search(pattern, issue) is not None

    def phrase_score(phrase):
        words = normalize_text(phrase).split()
        if len(words) >= 3:
            return 5
        elif len(words) == 2:
            return 3
        else:
            return 1

    with sqlite3.connect(DATABASE_NAME) as connection:
        connection.row_factory = sqlite3.Row
        rights = connection.execute(
            "SELECT * FROM legal_rights"
        ).fetchall()

    matches = []

    for right in rights:
        title = normalize_text(right["title"])
        keywords = right["keywords"].split("|")
        score = 0
        matched_phrases = set()
        for keyword in keywords:
            keyword = normalize_text(keyword)
            if keyword and phrase_matches(keyword):
                matched_phrases.add(keyword)
                score += phrase_score(keyword)

        for topic, expressions in synonyms.items():
            if topic in title:
                for expression in expressions:
                    expression = normalize_text(expression)
                    if (phrase_matches(expression) and expression not in matched_phrases):
                        matched_phrases.add(expression)
                        score += phrase_score(expression)

        if phrase_matches(title):
            score += 5

        meaningful_matches = [
            phrase for phrase in matched_phrases
            if len(phrase.split()) >= 2
        ]
        if meaningful_matches or phrase_matches(title):
            matches.append((score, dict(right)))    
            
    matches.sort(key=lambda item: item[0], reverse=True)
    if not matches:
        return []

    highest_score = matches[0][0]
    minimum_score = max(3, highest_score * 0.5)

    filtered = [
        right for score, right in matches
        if score >= minimum_score
    ]

    return filtered[:3]

def personalize_guidance(user_issue, results):
    if not results:
        return None

    issue = normalize_text(user_issue)
    categories = {right["category"] for right in results}

    if "Domestic Violence" in categories:
        introduction = (
            "I'm sorry you're experiencing difficulties at home. "
            "Your safety and wellbeing matter. There may be legal "
            "protections available to help you."
        )
    elif "Workplace Rights" in categories:
        introduction = (
            "I'm sorry you're facing this situation at work. "
            "You deserve to be treated with dignity and respect. "
            "Let's look at the protections and options that may apply."
        )
    elif "Marriage & Family" in categories:
        introduction = (
            "Family-related legal difficulties can be stressful. "
            "There may be legal options available to protect your "
            "rights and interests."
        )
    elif "Financial & Property Rights" in categories:
        introduction = (
            "Financial and property disputes can be difficult to navigate. "
            "Understanding your legal entitlements can help you "
            "decide what to do next."
        )
    elif "Safety & Protection" in categories:
        introduction = (
            "I'm sorry you're dealing with this situation. "
            "Your safety is important, and there may be steps "
            "you can take to seek protection."
        )
    else:
        introduction = (
            "I'm sorry you're facing this situation. "
            "You deserve to feel safe, respected, and supported. "
            "Let's explore the legal protections and practical steps "
            "that may be available to you."
        )

    concerns = [right["title"] for right in results[:3]]
    urgent_terms = [
        "kill me", "threatened to kill", "attack", "beating", "beats me",
        "hits me", "physical abuse", "unsafe", "immediate danger"
    ]
    urgent = any(term in issue for term in urgent_terms)

    question = (
        "Could you share when this happened and whether "
        "the situation is still ongoing?"
    )

    if "Domestic Violence" in categories:
        question = (
            "Are you currently in a safe place, "
            "and is the abuse or threatening behaviour ongoing?"
        )
    elif "Workplace Rights" in categories:
        question = (
            "Is this happening at your current workplace, "
            "and have you reported it to anyone?"
        )
    elif "Financial & Property Rights" in categories:
        question = (
            "What is your replationship to the property owner, "
            "and is the property inherited or self-acquired?"
        )
    return {
        "introduction": introduction,
        "concerns": concerns,
        "urgent": urgent,
        "question": question,
        "rights": results[:3]
}

def suggest_complaint_type(results, user_issue=""):
    complaint_mapping = {
        "Workplace Sexual Harassment": [
            "sexual harassment", "unwanted touching", "sexual advances"
        ],
        "Maternity Leave or Maternity Benefits Denial": [
            "maternity", "pregnancy", "maternity leave"
        ],
        "Unequal Pay or Unpaid Wages": [
            "equal pay", "unequal pay", "pay discrimination", "lower salary", "unpaid wages", "wage discrimination"
        ],
        "Workplace Discrimination or Unfair Treatment": [
            "workplace discrimination", "gender discrimination", "unfair treatment at work"
        ],
        "Domestic Violence": [
            "domestic violence", "physical abuse", "husband hits", "husband beats", "violence at home", "hits me", "beats me", "physically hurts me", "physical violence", "abusive husband"
        ],
        "Economic Abuse or Financial Control": [
            "economic abuse", "financial control", "controls my bank account", "takes my salary", "financial abuse"
        ],
        "Dowry Harassment": [
            "dowry", "dowry harassment", "in laws demand", "expensive gifts", "money from my parents"
        ],
        "Maintenance or Financial Support": [
            "maintenance", "financial support", "child support", "living expenses"
        ],
        "Marriage-Related Harassment or Cruelty": [
            "cruelty", "matrimonial cruelty", "marital cruelty"
        ],
        "Child Custody or Child-Related Concerns": [
            "child custody", "guardianship"
        ],
        "Property or Inheritance Rights Denial": [
            "inheritance", "property share", "ancestral property", "property rights"
        ],
        "Financial Exploitation or Fraud": [
            "financial fraud", "financial exploitation", "bank fraud"
        ],
        "Stridhan or Personal Property Withholding": [
            "stridhan", "jewellery withheld", "return my jewellery"
        ],
        "Stalking, Threats or Intimidation": [
            "stalking", "following me", "keeps calling", "criminal intimidation"
        ],
        "Cyber Harassment or Online Abuse": [
            "cyber harassment", "online abuse", "fake instagram", "fake account", "online threats"
        ],
        "Sexual Assault or Physical Harassment": [
            "sexual assault", "physical harassment", "sexual violence"
        ]
    }

    issue = normalize_text(user_issue)
    best_type = None
    best_score = 0

    for complaint_type, phrases in complaint_mapping.items():
        score = 0
        for phrase in phrases:
            phrase = normalize_text(phrase)
            if re.search(r"\b" + re.escape(phrase) + r"\b", issue):
                score += len(phrase.split())

        if score > best_score:
            best_score = score
            best_type = complaint_type

    if best_type:
        return best_type

    for right in results:
        title = normalize_text(right["title"])
        for complaint_type, phrases in complaint_mapping.items():
            for phrase in phrases:
                phrase = normalize_text(phrase)
                if re.search(r"\b" + re.escape(phrase) + r"\b", title):
                    return complaint_type

    return None