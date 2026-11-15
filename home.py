import streamlit as st

def show_home():
    def open_category(category_name):
        st.session_state["selected_category"] = category_name
        st.session_state["page"] = "Explore Rights"

    #Welcome section
    left, right = st.columns([1, 1], gap="small")

    with left:
        st.markdown("""
            <div style="padding-top: 35px;">
                <h1 style="font-family: Georgia, serif; font-size: clamp(40px, 5vw, 64px); 
                font-weight: 800; color: #702F46; margin: -30px 0 0 0;">
                    HerRights <span style="font-size: 50px;"> ⚖️</span>
                </h1>
                <p style="color: #456B5A; font-size: 16px; font-weight: 700;
                letter-spacing: 2px; margin-bottom: 25px;">
                    EMPOWERMENT THROUGH AWARENESS
                </p>
                <h2 style="font-family: Georgia, serif; font-size: 45px;
                line-height: 1.3; color: #702F46; margin-bottom: 15px;">
                    Know Your Rights. <br>
                    <span style="color: #456B5A;">
                        Claim Your Space.
                    </span>
                </h2>
                <p style="font-size: 16px; line-height: 1.5; color: #51484B;
                max-width: 450px; margin-bottom: 20px;">
                    HerRights is a legal awareness platform designed to help women
                    understand their legal rights under Indian law, explore 
                    available protections, and take informed steps towards justice.
                </p>
            </div>
        """,unsafe_allow_html=True)

        # st.markdown(
        #     "<h1 style='font-size: 65px;'> HerRights ⚖️</h1>",
        #     unsafe_allow_html=True
        # )

        # st.markdown(
        #     "<h3>Know Your Rights. Claim your Space.</h3>",
        #     unsafe_allow_html=True
        # )

        # st.write(
        #     "HerRights is a legal awareness platform designed to help "
        #     "women understand their rights under Indian law."
        # )

    with right:
        st.image("assets/hero.png", use_container_width=True)

    #Rights categories
    st.markdown(
        "<h2 style='text-align: center;'>Explore by Category</h2>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<p style='text-align: center;'>"
        "Learn about your rights, relevant laws, and the actions you "
        "can take based on your situation."
        "</p>",
        unsafe_allow_html=True
    )
    st.write("")

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
    columns = st.columns(5, gap="small")
    for col, (title, description) in zip(columns, categories):
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