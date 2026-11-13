import streamlit as st

def show_navigation():
    page = st.radio(
        "Navigation",
        ["Home", "Explore Rights", "Legal Guidance", "Help & Support"],
        horizontal=True,
        label_visibility="collapsed"
    )
    return page