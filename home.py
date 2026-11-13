import streamlit as st

def show_home():
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
    st.write(
        "HerRights is a legal awareness platform designed "
        "to help women understand their rights unders Indian law."
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

        ("💰 Financial & Property",
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
                    st.subheader(title)
                    st.write(description)