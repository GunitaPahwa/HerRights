import streamlit as st
from database import get_rights_by_category

def show_explore_rights():
    st.title("Explore Your Rights")
    st.write("Learn about your legal rights under Indian law.")
    categories = ["Workplace Rights", "Domestic Violence", "Marriage & Family",
                  "Financial & Property Rights", "Safety & Protection"]

    selected_category = st.session_state.pop("selected_category", None)
    if selected_category in categories:
        st.session_state["explore_category"] = selected_category
    elif "explore_category" not in st.session_state:
        st.session_state["explore_category"] = categories[0]

    category = st.selectbox(
        "Select a category:",
        categories,
        key="explore_category"
    )

    # st.write("DEBUG - Selected category:", selected_category)
    # st.write("DEBUG - Dropdown category:", category)
    rights = get_rights_by_category(category)
    if rights:
        for title, description, law, source_url in rights:
            with st.container(border=True, key=f"rights_card_{category}_{title}"):
                st.markdown(
                    f"<h3 style='font-family: Georgia, serif; font-size: 24px; "
                    f"color: #702F46; margin: -5px 0 -5px 0;'>{title}</h3>",
                    unsafe_allow_html=True
                )
                st.markdown(
                    f"<p style='margin: 0 0 10px 0; line-height: 1.5;'>{description}</p>",
                    unsafe_allow_html=True
                )
                st.markdown(f"""
                    <div style="background-color: #EAE5DD; border-radius: 8px; 
                    padding: 5px 16px; margin: 0 230px 12px 0; font-size: 14px;">
                        <span style="color: #702F46; font-weight: 600;">
                            Applicable Law:
                        </span>
                        <span style="color: #342D30;">
                            {law}
                        </span>
                    </div>
                """, unsafe_allow_html=True)

                if source_url:
                    st.link_button(
                        "View Official Legal Source",
                        source_url,
                        icon=":material/menu_book:"
                    )

    else:
        st.info("Legal information for this category will be added soon.")                