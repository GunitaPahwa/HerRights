import streamlit as st

def show_navigation():
    pages = ["Home", "Explore Rights", "Legal Guidance", "Complaint Generator", "Help & Support"]
    
    if "page" not in st.session_state:
        st.session_state["page"] = "Home"
    
    return st.radio(
        "Navigation",
        pages,
        horizontal=True,
        key="page",
        label_visibility="collapsed"
    )