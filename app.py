import streamlit as st

#Import fucntions from our other Python files
from styles import apply_styles
import importlib
import styles
importlib.reload(styles)

from home import show_home
from navigation import show_navigation
from database import create_database, import_legal_data, get_rights_by_category
from guidance import get_legal_guidance, personalize_guidance

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
st.divider()

#Homepage
if page == "Home":
    show_home()

#Explore rights page
elif page == "Explore Rights":
    st.title("Explore Your Rights")
    st.write("Learn about your legal rights under Indian law.")

    categories = [
        "Workplace Rights",
        "Domestic Violence",
        "Marriage & Family",
        "Financial & Property Rights",
        "Safety & Protection"
    ]

    selected_category = st.selectbox(
        "Select a category:",
        categories
    )

    rights = get_rights_by_category(selected_category)
    if rights:
        for title, description, law in rights:
            with st.container(border=True):
                st.subheader(title)
                st.write(description)
                st.caption(f"Applicable Law: {law}")
    else:
        st.info("Legal information for this category will be added soon.")
    
#Legal guidance page
elif page == "Legal Guidance":
    st.title("Get Legal Guidance")
    st.write("Describe your situation to understand your "
             "legal rights and possible next steps.")

    user_issue = st.text_area(
        "Describe the issue you are facing:",
        placeholder="Explain your situation here...",
        height=150
    )

    if st.button("Get Guidance"):
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
                for concern in guidance["concerns"]:
                    st.write(f"• {concern}")

                st.markdown("### What You Can Do Next")
                for number, right in enumerate(guidance["rights"], start=1):
                    with st.container(border=True):
                        st.markdown(f"**{number}. {right['title']}**")
                        st.write(right["recommended_actions"])
                        
                        with st.expander("View legal rights and possible remedies."):
                            st.write(right["description"])
                            st.write(f"**Applicable Law:** {right['law']}")
                            st.write(
                                f"**Possible Remedies:** "
                                f"{right['possible_remedies']}"
                            )
                            st.write(f"**References:** {right['source_url']}")

                st.markdown("### A Question to Help You Further")
                st.info(guidance["question"])
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

#Help and support page
elif page == "Help & Support":
    st.title("Help & Support")
    st.write("Find legal aid services, helplines, "
             "and official support resources.")
    st.info("Verified support resources will be added soon.")

#Footer
st.divider()

st.caption(
    "© HerRights | Women's Legal Rights Awareness Platform | "
    "For educational purposes only."
)