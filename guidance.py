import re
import sqlite3
from database import DATABASE_NAME

def normalize_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return " ".join(text.split())

def get_legal_guidance(user_issue):
    issue = normalize_text(user_issue)

    synonyms = {
        "maintenance": [
            "financial support", "living expenses", 
            "refuses to provide money", "husband left me", 
            "support our child", "child support", "abondoned me"
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
            "following me", "follows me", "keeps calling", 
            "unwanted calls", "waiting outside", "tracking me",
            "multiple messages"
        ],
        "inheritance": [
            "property share", "father passed away", "inherit property",
            "brother refuses property", "ancestral property", 
            "father's property", "family property", "inheritance denied",
            "share of the property", "daughter property rights"
        ]
    }

    with sqlite3.connect(DATABASE_NAME) as connection:
        connection.row_factory = sqlite3.Row
        rights = connection.execute(
            "SELECT * FROM legal_rights"
        ).fetchall()

    matches = []

    for right in rights:
        keywords = right["keywords"].split("|")
        title = normalize_text(right["title"])
        score = 0
        for keyword in keywords:
            keyword = normalize_text(keyword)
            if keyword and re.search(r"\b" + re.escape(keyword) + r"\b", issue):
                score += 2

        for legal_topic, expressions in synonyms.items():
            if legal_topic in title:
                for expression in expressions:
                    expression = normalize_text(expression)
                    if re.search(r"\b" + re.escape(expression) + r"\b", issue):
                        score += 3

        if score > 0:
            matches.append((score, dict(right)))

    matches.sort(key=lambda item: item[0], reverse=True)

    return [right for score, right in matches[:3]]

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
            "Let's explore the legal protections adn practical steps "
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