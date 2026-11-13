import streamlit as st

#Configure the website
st.set_page_config(
    page_title="HerRights",
    page_icon="⚖️",
    layout="wide"
)

#Homepage
st.title("⚖️ HerRights")
st.subheader("Know Your Rights. Understand Your Options.")

st.write(
    "Empowering women through legal awareness "
    "and accessible guidance on Indian laws."
)

st.divider()

#Legal rights categories
categories = [
    "Workplace Rights",
    "Domestic Violence",
    "Marriage and Family",
    "Financial and Property Rights",
    "Safety and Protection"
]

selected_category = st.selectbox(
    "Select a category:",
    categories
)

st.info(f"You selected: {selected_category}")

st.divider()

#Legal guidance section
st.header("Get Legal Guidance")

user_issue = st.text_area(
    "Describe your situation:",
    placeholder="Explain the issue you're facing..."
)

if st.button("Get Guidance"):
    if user_issue.strip():
        st.success("Your issue has been submitted!")
        st.write("Legal guidance will appear here.")
    else:
        st.warning("Please describe your issue first.")

