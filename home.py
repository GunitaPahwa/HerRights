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
                <h1 style="font-family: Georgia, serif; font-size: clamp(60px, 10vw, 100px); 
                font-weight: 800; color: #702F46; margin: -30px 0 0 0;">
                    HerRights
                </h1>
                <p style="color: #456B5A; font-size: 16px; font-weight: 700; line-height: 15px;
                letter-spacing: 8px; margin-bottom: 25px;">
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

    with right:
        st.image("assets/hero.png", use_container_width=True)

    st.divider()
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
        (" Workplace Rights",
        "Know your rights at work, including safety, equality, and protection from harassment."),

        (" Domestic Violence",
        "Get information on legal protection, immediate support, and remedies for domestic abuse."),

        (" Marriage & Family",
        "Understand your rights related to marriage, divorece, maintenance, and child custody."),

        (" Financial & Property Rights",
        "Learn about your rights to property, inheritance, maintenance, and financial independence."),

        (" Safety & Protection",
        "Find laws and support for your safety in public, private, and online spaces.")
    ]

    #Display categories in three columns
    first_row = st.columns(3, gap="medium")
    second_row = st.columns([1, 2, 2, 1], gap="medium")
    card_columns = first_row + [second_row[1], second_row[2]]
    icon_files = [
        "workplace.png", "domestic.png", "marriage.png", "financial.png", "safety.png"
    ]
    for col, (title, description), icon_file in zip(card_columns, categories, icon_files):
        with col:
            with st.container(border=True):
                icon_col, title_col = st.columns(
                    [1, 3.5], gap="small", vertical_alignment="center"
                )
                with icon_col:
                    st.image(f"assets/{icon_file}", use_container_width=True)
                with title_col:
                    st.markdown(
                        f"<h3 style='font-family: Georgia, serif; font-size: 24px; font-weight: bold; color: #702F46; margin: 0;'>"
                        f"{title}</h3>",
                        unsafe_allow_html=True
                    )

                st.markdown(
                    f"<div style='min-height: 55px; line-height: 1.5;'>{description}</div>",
                    unsafe_allow_html=True
                )
                category_name = title.strip()
                st.button(
                    "Explore Rights",
                    icon=":material/arrow_forward:",
                    icon_position="right",
                    key=f"home_{category_name}",
                    use_container_width=True,
                    on_click=open_category,
                    args=(category_name,)
                )