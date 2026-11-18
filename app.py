import streamlit as st

#Import functions from our other Python files
from styles import apply_styles
import importlib
import styles
importlib.reload(styles)

from home import show_home
from navigation import show_navigation
from database import create_database, import_legal_data, get_rights_by_category
from explore_rights import show_explore_rights
from guidance import get_legal_guidance, personalize_guidance, suggest_complaint_type
from complaint import generate_complaint, get_submission_guidance
from support import show_support
from html import escape
import re
from datetime import datetime

def extract_incident_date(text):
    patterns = [
        r"\b\d{1,2}/\d{1,2}/\d{4}\b",
        r"\b\d{1,2}\s+[A-Za-z]+\s+\d{4}\b"
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            for date_format in ("%d/%m/%Y", "%d %B %Y", "%d %b %Y"):
                try:
                    return datetime.strptime(match.group(), date_format).date()
                except ValueError:
                    continue
    return None

def extract_incident_location(text):
    patterns = [
        r"\b(?:incident occurred|incident happened|happened|occurred)\s(?:at|in)\s+([A-Za-z ]+?)(?:[.,]|$)",
        r"\b(?:at our|at my|in our|in my)\s(home|house|workplace|company|office)\b",
        r"\blive\b[^.!?]{0,80}?\bin\s+([A-Za-z ]+?)(?:[.,]|$)",
        r"\bresid(?:e|ing)\s+in\s+([A-Za-z ]+?)(?:[.,]|$)"
    ]
    for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(1).strip()
    return ""

#Configure the website
st.set_page_config(
    page_title="HerRights",
    page_icon="⚖️",
    layout="wide"
)
styles.apply_styles() 
create_database()
import_legal_data()

#Homepage
page = show_navigation()

#Homepage
if page == "Home":
    show_home()

#Explore rights page
elif page == "Explore Rights":
    show_explore_rights()

#Legal guidance page
elif page == "Legal Guidance":
    st.title("Get Legal Guidance")
    st.write("Describe your situation to understand your "
             "legal rights and possible next steps.")

    user_issue = st.text_area(
        "Describe the issue you are facing:",
        placeholder=(
            "For example: I am facing harassment at my workplace and "
            "want to understand my legal rights and options..."
        ),
        height=150
    )
    st.caption(
        "🔒 For your privacy, avoid sharing sensitive personal details "
        "such as your full address, phone number, or identification numbers."
    )

    if st.button("Get Guidance", key="get_guidance_btn"):
        if not user_issue.strip():
            st.warning("Please describe your issue first.")
        else:
            results = get_legal_guidance(user_issue)
            guidance = personalize_guidance(user_issue, results)
            if guidance:
                st.markdown("### Your Personalized Guidance")
                st.write(guidance["introduction"])
                if guidance["urgent"]:
                    st.error(
                        "Your description may indicate an immediate "
                        "safety concern. If you are in immediate danger "
                        "in India, call 112 or seek a safe location."
                    )

                st.markdown("### Understanding Your Situtation")
                st.write("Based on your description, these issues may be relevant.")
                concerns_html = "".join(
                    f'<span class="guidance-tag">{escape(concern)}</span>'
                    for concern in guidance["concerns"]
                )
                st.markdown(
                    f'<div class="guidance-tags">{concerns_html}</div>',
                    unsafe_allow_html=True
                )

                st.markdown("### What You Can Do Next")
                for number, right in enumerate(guidance["rights"], start=1):
                    with st.container(border=True, key=f"guidance_right_{number}"):
                        st.markdown(
                            f"<div style='font-family: Georgia, serif; font-size: 21px; "
                            f"font-weight: bold; color: #702F46;'>"
                            f"{number}. {escape(right['title'])}</div>",
                            unsafe_allow_html=True
                        )
                        st.write(right["recommended_actions"])
                        
                        with st.expander("View legal rights and possible remedies."):
                            st.write(right["description"])
                            st.write(f"**Applicable Law:** {right['law']}")
                            st.write(
                                f"**Possible Remedies:** "
                                f"{right['possible_remedies']}"
                            )
                            if right["source_url"]:
                                st.link_button(
                                    "View Official Legal Source",
                                    right["source_url"],
                                    icon=":material/menu_book:"
                                )

                st.markdown("### A Moment to Reflect")
                st.write("As you consider your next steps, think about this question:")
                st.markdown(
                    f"""
                        <div class="guidance-question">{escape(guidance["question"])}</div>
                """, unsafe_allow_html=True)
                st.caption(
                    "You don't need to answer here. This question is intended to help "
                    "you consider your situation and what support you may need."
                )

                st.subheader("Need to Take Action?")
                suggested_type = suggest_complaint_type(results, user_issue)
                
                def open_complaint_generator():
                    st.session_state["suggested_complaint_type"] = suggested_type
                    st.session_state["complaint_issue"] = user_issue
                    st.session_state["complaint_issue_recipient_pending"] = True
                    st.session_state["page"] = "Complaint Generator"
                
                st.button(
                    "Generate Complaint", 
                    key="guidance_complaint", 
                    on_click=open_complaint_generator
                )   

                st.caption(
                    "This guidance identifies possible legal options based on "
                    "limited information. Eligibility, procedures and appropriate "
                    "next steps depend on the facts and applicable law."
                )

            else:
                st.info(
                    "We couldn't confidently identify the legal issues from your "
                    "description. Please provide more specific the issue using more "
                    "specific details. This does not mean you have no legal rights."
                )            

#Complaint generator page
elif page == "Complaint Generator":
    st.title("Complaint Generator")
    st.write(
        "Create a formal complaint based on your situation. "
        "You can review and edit it before downloading."
    )

    complaint_types = [
        "Workplace Sexual Harassment",
        "Workplace Discrimination or Unfair Treatment",
        "Maternity Leave or Maternity Benefits Denial",
        "Unequal Pay or Unpaid Wages",
        "Domestic Violence",
        "Economic Abuse or Financial Control",
        "Dowry Harassment",
        "Maintenance or Financial Support",
        "Marriage-Related Harassment or Cruelty",
        "Child Custody or Child-Related Concerns",
        "Property or Inheritance Rights Denial",
        "Stridhan or Personal Property Withholding",
        "Stalking, Threats or Intimidation",
        "Cyber Harassment or Online Abuse",
        "Sexual Assault or Physical Harassment"
    ]
    suggested_type = st.session_state.pop("suggested_complaint_type", None)
    if suggested_type in complaint_types:
        st.session_state["complaint_type_selection"] = suggested_type

    if "complaint_type_selection" not in st.session_state:
        st.session_state["complaint_type_selection"] = None

    complaint_type = st.selectbox(
        "Select complaint type:",
        complaint_types,
        index=None,
        placeholder="Choose a complaint type",
        key="complaint_type_selection"
    )
    if complaint_type is None:
        st.info("Please select a complaint type to continue.")
        st.stop()
    
    recipient_suggestions = {
        "Workplace Sexual Harassment": "Internal Committee (IC)",
        "Workplace Discrimination or Unfair Treatment": "HR Department",
        "Maternity Leave or Maternity Benefits Denial": "HR Department",
        "Unequal Pay or Unpaid Wages": "Employer / Labour Authority",
        "Domestic Violence": "Protection Officer",
        "Economic Abuse or Financial Control": "Protection Officer",
        "Dowry Harassment": "Station House Officer",
        "Maintenance or Financial Support": "Appropriate Family Court",
        "Marriage-Related Harassment or Cruelty": "Protection Officer / Police",
        "Child Custody or Child-Related Concerns": "Appropriate Family Court",
        "Property or Inheritance Rights Denial": "Legal Aid Authority",
        "Stridhan or Personal Withholding": "Police / Protection Officer",
        "Stalking, Threats or Intimidation": "Station House Officer",
        "Cyber Harassment or Online Abuse": "Cyber Crime Police",
        "Sexual Assault or Physical Harassment": "Station House Officer"
    }
    if "complaint_recipient" not in st.session_state:
        st.session_state["complaint_recipient"] = ""
    if st.session_state.pop("complaint_issue_recipient_pending", False):
        st.session_state["complaint_recipient"] = recipient_suggestions.get(complaint_type, "")
    
    name_col, recipient_col = st.columns(2, gap="medium")
    with name_col:
        name = st.text_input("Your Full Name")
    with recipient_col:
        recipient = st.text_input(
            "Recipient / Authority",
            placeholder="e.g., Station House Officer, Police Station",
            key="complaint_recipient"
        )

    transferred_issue = st.session_state.get("complaint_issue")
    if transferred_issue:
        extracted_date = extract_incident_date(transferred_issue)
        if extracted_date:
            st.session_state["complaint_incident_date"] = extracted_date
        
        extracted_location = extract_incident_location(transferred_issue)
        if extracted_location:
            st.session_state["complaint_incident_location"] = extracted_location

    if "complaint_incident_date" not in st.session_state:
        st.session_state["complaint_incident_date"] = None
    if "complaint_incident_location" not in st.session_state:
        st.session_state["complaint_incident_location"] = ""
    
    date_col, location_col = st.columns(2, gap="medium")
    with date_col:
        incident_date = st.date_input(
            "Date of Incident",
            key="complaint_incident_date",
            value=None,
            format="DD/MM/YYYY"
        )
    with location_col:
        incident_location = st.text_input(
            "Location of Incident",
            key="complaint_incident_location"
        )
    
    address = st.text_area("Your Address", height=70)

    if "complaint_description" not in st.session_state:
        st.session_state["complaint_description"] = ""
    
    transferred_issue = st.session_state.pop("complaint_issue", None)
    if transferred_issue is not None:
        st.session_state["complaint_description"] = transferred_issue

    description = st.text_area(
        "Describe What Happened",
        height=180,
        placeholder="Explain the incident clearly and factually...",
        key="complaint_description"
    )
    requested_action = st.text_area(
        "What Action Would You Like to Request?",
        height=100,
        placeholder="Describe the assistance or action you are seeking..."
    )

    if st.button("Generate Complaint", key="guidance_complaint"):
        if not all([name.strip(), address.strip(), recipient.strip(),
                    incident_location.strip(), description.strip()]):
            st.warning("Please complete the required details.")
        
        else:
            st.session_state["complaint_draft"] = generate_complaint(
                complaint_type, name, address, recipient, 
                incident_date.strftime("%d/%m/%Y") if incident_date else "Not specified",
                incident_location, description, requested_action
            )

    st.divider()
    st.subheader("Where to Submit Your Complaint")
    authority, instructions, notes = get_submission_guidance(complaint_type)
    with st.container(key="submission_card"):
        st.markdown(
            f"""
            <div class="submission-content">
                <div class="submission-section">
                    <div class="submission-label">⚖ Relevant Authority</div>
                    <p>{escape(authority)}</p>
                </div>
                <div class="submission-separator"></div>
                <div class="submission-section">
                    <div class="submission-label">▤ How to Submit</div>
                    <p>{escape(instructions)}</p>
                </div>
                <div class="submission-important">
                    <p>&#x1F6C8;<strong> Important:</strong> {escape(notes)}</p>
                </div>
            </div>
            """, unsafe_allow_html=True
        )
    
    if "complaint_draft" in st.session_state:
        st.subheader("Review Your Complaint")
        st.text_area(
            "Review and edit your complaint before downloading:",
            key="complaint_draft",
            height=350
        )
        st.download_button(
            "Download Complaint (.txt)",
            data=st.session_state["complaint_draft"],
            file_name="HerRights_Complaint.txt",
            mime="text/plain",
            icon=":material/download:",
            key="download_complaint"
        )
        st.info(
            "This is an editable complaint draft, not an official filing. "
            "Check the appropriate authority and submission requirements "
            "before using it."
        )

#Help and support page
elif page == "Help & Support":
    show_support()

#Footer
st.divider()

st.caption(
    "© HerRights | Women's Legal Rights Awareness Platform | "
    "For educational purposes only."
)