import streamlit as st

def show_navigation():
    pages = ["Home", "Explore Rights", "Legal Guidance", "Complaint Generator", "Help & Support"]
    page_icons = {
        "Home": "⌂",
        "Explore Rights": "☷",
        "Legal Guidance": "§",
        "Complaint Generator": "✎",
        "Help & Support": "♡"
    }
    
    if "page" not in st.session_state:
        st.session_state["page"] = "Home"

    logo_col, nav_col = st.columns([1,4], gap="small", vertical_alignment="center")
    with logo_col:
        brand_icon, brand_name = st.columns([1, 2.8], gap="small", vertical_alignment="center")
        with brand_icon:
            st.image("assets/logo.png", width=65)

        with brand_name:
            st.markdown("""
                <div style='font-family: Georgia, serif; font-size: 25px; font-weight: bold; color: #702F46; line-height: 1; transform: translateY(-8px);'>HerRights</div>
            """,unsafe_allow_html=True)

    with nav_col:
        with st.container(horizontal=True, horizontal_alignment="right"):
            selected_page = st.segmented_control(
                "Navigation",
                options=pages,
                format_func=lambda page: f"{page_icons[page]} {page}",
                key="page",
                label_visibility="collapsed",
                width="content"
            )

        return selected_page