import streamlit as st
def apply_styles():
    st.markdown("""
    <style>
        /* main website bg */
        .stApp {
            background-color: #F6F3EA;
            color: #342D30;
        }

        /* headings */
        .stApp h1,
        .stApp h2,
        .stApp h3 {
            color: #702F46 !important;
            font-family: Georgia, serif;
        }

        /* general text */
        .stApp p{
            color: #342D30;
        }

        /* buttons */
        div.stButton > button {
            background-color: #456B5A;
            color: white;
            border-radius: 12px;
            border: none;
            padding: 10px 24px;
        }

        div.stButton > button:hover {
            background-color: #345344;
            color: white;
        }

        /* info boxes */
        div[data-testid="stAlert"] {
            background-color: #E5EDE7;
            border-radius: 12px;
            border-left: 4px solid #456B5A;
        }

        div[data-testid="stAlert"] p {
            color: #342D30 !important;
        }

        /* Navigation bar */
        div[role="radiogroup"] {
            background-color: #FFFFFF;
            padding: 12px 18px;
            border-radius: 15px;
            border: 1px solid #E9E0DC;
            gap: 12px;
        }

        div[role="radiogroup"] label {
            background-color: #F6F3EA;
            border-radius: 10px;
            padding: 8px 16px;
            cursor: pointer;
        }

        div[role="radiogroup"] label p {
            color:  #702F46 !important;
            font-weight: 600;
        }

        div[role="radiogroup"] label:has(input:checked) {
            background-color: #456B5A;
        }

        div[role="radiogroup"] label:has(input:checked) p {
            color: #FFFFFF !important;
        }

        div[data-testid="stVerticalBlockBorderWrapper"] {
            border-color: #D9A7B0;
        }
    </style>    
    """, unsafe_allow_html=True)