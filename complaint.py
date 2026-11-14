from datetime import date

def generate_complaint(complaint_type, name, address, recipient, incident_date, 
                       incident_location, description, requested_action):
    today = date.today().strftime("%d/%m/%Y")

    subjects = {
        "Workplace Sexual Harassment":
            "Formal Complaint Regarding Workplace Sexual Harassment",

        "Workplace Discrimination or Unfair Treatment":
            "Complaint Regarding Workplace Discrimination",

        "Maternity Leave or Maternity Benefits Denial":
            "Complaint Regarding Denial of Maternity Benefits",

        "Unequal Pay or Unpaid Wages":
            "Complaint Regarding Unequal Pay or Unpaid Wages",

        "Domestic Violence":
            "Complaint Regarding Domestic Violence",

        "Economic Abuse or Financial Control":
            "Complaint Regarding Economic Abuse",

        "Dowry Harassment":
            "Complaint Regarding Dowry Harassment",

        "Maintenance or Financial Support":
            "Request for Maintenance or Financial Support",

        "Marriage-Related Harassment or Cruelty":
            "Complaint Regarding Matrimonial Harassment",

        "Child Custody or Child-Related Concerns":
            "Application Regarding Child-Related Concerns",

        "Property or Inheritance Rights Denial":
            "Complaint Regarding Property or Inheritance Rights",

        "Financial Exploitation or Fraud":
            "Complaint Regarding Financial Exploitation",

        "Stridhan or Personal Property Withholding":
            "Request for Return of Stridhan or Personal Property",

        "Stalking, Threats or Intimidation":
            "Complaint Regarding Stalking or Threats",

        "Cyber Harassment or Online Abuse":
            "Complaint Regarding Cyber Harassment",

        "Sexual Assualt or Physical Harassment":
            "Complaint Regarding Sexual or Physical Assault"
    }

    subject = subjects.get(
        complaint_type, "Formal Complaint Regarding Legal Concerns"
    )

    complaint = f"""
Date: {today}

To,
{recipient}

Subject: {subject}

Respected Sir/Madam,

I, {name}, residing at {address}, wish to bring the following matter to your attention. 

Date of Incident: {incident_date}
Location of Incident: {incident_location}

Description of the Incident:
{description}

I request that the matter be examined and that appropriate action be taken in accordance with applicable law.

Requested Action:
{requested_action}

I am willing to provide further information or supporting documents, where available and appropriate.

Thank you for considering this complaint.

Yours faithfully,

{name}
Address: {address}
"""

    return complaint.strip()

def get_submission_guidance(complaint_type):
    guidance = {
        "Workplace Sexual Harassment":(
            "Internal Committee (IC) or Local Committee (LC)",
            "Submit a written complaint to your workplace's Internal "
            "Committee. Where applicable, approach the district "
            "Local Committee.",
            "The POSH Act generally provides a three-month complaint "
            "period, with a possible extension of up to three "
            "additional months in qualifying cases."
        ),
    
        "Workplace Discrimination or Unfair Treatment":(
            "Employer HR Department or Relevant Labour Authority",
            "Raise the concern with HR or the appropriate workplace "
            "grievance authority. Depending on the issue, you may "
            "approach the labour authority.",
            "Keep copies of relevant communications, policies and "
            "employment records."
        ),
        
        "Maternity Leave or Maternity Benefits Denial":(
            "Employer HR Department or Maternity Benefit Inspector",
            "Submit a written request to your employer. For disputes "
            "covered by the Maternity Benefit Act, approach the "
            "appointed Inspector.",
            "Eligibility and the applicable procedure depend on your "
            "employment circumstances and governing law."
        ),
        
        "Unequal Pay or Unpaid Wages":(
            "Employer or Relevant Labour Authority",
            "Raise the issue with your employer and, where "
            "appropriate, approach the elevant labour authority or "
            "statutory claims mechanism.",
            "Preserve salary slips, employment contracts and "
            "records of unpaid wages."
        ),
        
        "Domestic Violence":(
            "Protection Officer, Police or Magistrate",
            "Contact a Protection Officer or seek legal aif for an "
            "application under the Domestic Violence Act. Police can "
            "be contacted for immediate safety concerns or suspected offences.",
            "Depending on the facts, protection, residence and monetary "
            "relief may be available."
        ),
        
        "Economic Abuse or Financial Control":(
            "Protection Officer, Legal Aid or Magistrate",
            "Where economic abuse occurs in a domestic relationship, "
            "seek help from a Protection Officer or legal aid service "
            "regarding available remedies.",
            "Economic abuse can fall within the Domestic Violence Act. "
            "Other financial disputes may require a different legal process."    
        ),
        
        "Dowry Harassment":(
            "Police, Protection Officer or Legal Aid",
            "Report suspected dowry-related offences to the police. "
            "You may also seek protection and other relief under "
            "applicable domestic violence laws.",
            "Preserve messages, demand records and other evidence when "
            "it is safe to do so."
        ),
        
        "Maintenance or Financial Support":(
            "Family Court or Appropriate Magistrate",
            "Consult a legal aid service or lawyer about filing the "
            "appropriate maintenance application before the competent court.",
            "A general complaint letter may not be enough. The correct "
            "application depends on the relationship and applicable law."
        ),
      
        "Marriage-Related Harassment or Cruelty":(
            "Police, Protection Officer or Family Court",
            "Depending on the conduct involved, seek police assistance "
            "domestic violence relief or advice on available family "
            "court proceedings.",
            "Different remedies have different procedures. Not every "
            "marital dispute is a criminal offence."
        ),
       
        "Child Custody or Child-Related Concerns":(
            "Family Court or Competent Court",
            "Seek legal advice about filing an appropriate custody, "
            "guardianship or child-related applcation before the "
            "competent court.",
            "The child's welfare is central to custody decisions. A complaint "
            "letter alone generally does not initiate a custody proceeding."
        ),
       
        "Property or Inheritance Rights Denial":(
            "Civil Court, Legal Aid or Police if an Offence Occurred",
            "Seek legal advice about inheritance, partition or other "
            "appropriate civil proceedings. Contact police if seperate "
            "criminal conduct is involved.",
            "Inheritance rights depend on applicable personal law, "
            "property type and other facts."
        ),
        
        "Financial Exploitation or Fraud":(
            "Police or Appropriate Financial Regulator",
            "Report suspected fraud to the police or relevant financial "
            "institution or regulator. For online financial fraud, use "
            "the National Cyber Crime Reporting Portal.",
            "Contact your bank promptly if funds or account access may "
            "be at risk."
        ),
      
        "Stridhan or Personal Property Withholding":(
            "Police, Protection Officer or Legal Aid",
            "Seek legal advice about recovering stridhan or personal "
            "property. Depending on the facts, police reporting or domestic "
            "violence remedies may be appropriate.",
            "Keep an inventory and any available proof of ownership or possession."
        ),
        
        "Stalking, Threats or Intimidation":(
            "Police",
            "Report suspected stalking or criminal threats to the police. "
            "Seek immediate assistance if you are in danger.",
            "Save relevant messages, call records and incident details when safe."
        ),
        
        "Cyber Harassment or Online Abuse":(
            "Cyber Crime Police or National Cyber Crime Portal",
            "Report suspected cybercrime through cybercrime.gov.in or "
            "the appropriate cybercrime police unit.",
            "Preserve screenshots, URLs, usernames and timestamps when "
            "safe. Avoid sharing sensitive evidence publicly."
        ),
    
        "Sexual Assualt or Physical Harassment":(
            "Police or Emergency Services",
            "Contact police to report suspected offences, Seek medical "
            "assistance and safety support as needed.",
            "If you are in immediate danger, call 112. A formal "
            "complaint draft is not required before seeking urgent help."
        )
    }

    return guidance.get(complaint_type, (
        "Appropriate Legal Authority", 
        "Seek guidance from a qualified legal aid service or relevant authority.",
        "The correct procedure depends on your situation." 
        )
    )