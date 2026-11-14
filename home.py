import streamlit as st

def show_home():
    def open_category(category_name):
        st.session_state["selected_category"] = category_name
        st.session_state["page"] = "Explore Rights"
    #Welcome section
    st.markdown(
        "<h1 style='text-align:center;'> HerRights ⚖️</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h3 style='text-align:center;'>"
        "Know Your Rights. Understand Your Options."
        "</h3>",
        unsafe_allow_html=True
    )

    st.write("")
    st.markdown(
        "<p style='text-align:center;'>"
        "HerRights is a legal awareness platform designed "
        "to help women understand their rights unders Indian law."
        "</p>"
    )

    st.divider()

    #Rights categories
    st.header("Explore Your Rights")

    categories = [
        ("💼 Workplace Rights",
        "Harassment, discrimination and maternity benefits"),

        ("🏡 Domestic Violence",
        "Protection against domestic abuse"),

        ("💍 Marriage & Family",
        "Marriage, divorce, maintenance and custody"),

        ("💰 Financial & Property Rights",
        "Inheritance, property and financial rights"),

        ("🛡️ Safety & Protection",
        "Stalking, harassment and personal safety")
    ]

    #Display categories in three columns
    for i in range(0, len(categories), 3):
        columns = st.columns(3)

        for col, (title, description) in zip(columns, categories[i:i+3]):
            with col:
                with st.container(border=True):
                    st.markdown(
                        f"<div style='height: 85px; display: flex; align-items: center;'>"
                        f"<h3 style='font-size: 20px;'>{title}</h3>"
                        f"</div>",
                        unsafe_allow_html=True
                    )
                    st.markdown(
                        f"<div style='min-height: 75px;'>{description}</div>",
                        unsafe_allow_html=True
                    )

                    category_name = title.split(" ", 1)[1]
                    st.button(
                        "Explore Rights",
                        key=f"home_{category_name}",
                        use_container_width=True,
                        on_click=open_category,
                        args=(category_name,)
                    )