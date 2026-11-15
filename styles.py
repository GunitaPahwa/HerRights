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
            background-color: #87AA94;
            color: #342D30;
            border-radius: 12px;
            border: none;
            padding: 10px 24px;
        }

        div.stButton > button:hover {
            background-color: #A5C1AE;
            color: #342D30;
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
        button[data-variant="segmented_control"] {
            border: none !important;
            border-radius: 5px !important;
            background-color: transparent !important;
            padding: 10px 15px !important;
            margin: 0 !important;
        }

        button[data-variant="segmented_control"] p {
            color: #702F46 !important;
            font-weight: 600 !important;
            font-size: 15px;
            white-space: nowrap;
        }

        button[data-variant="segmented_control"][data-selected="true"],
        button[data-variant="segmented_control"][aria-checked="true"] {
            background-color: #456B5A !important;
            border-radius: 5px !important;
        }

        button[data-variant="segmented_control"][data-selected="true"] p,
        button[data-variant="segmented_control"][aria-checked="true"] p {
            color: #FFFFFF !important;
        }

        button[data-variant="segmented_control"]:not([data-selected="true"]):hover {
            background-color: #F1E9E5 !important;
        }

        div[data-testid="stButtonGroup"] div[role="radiogroup"] {
            display: flex !important;
            align-items: center;
            justify-content: flex-start;
            gap: 12px !important;
            background-color: #FFF9F5 !important;
            border: 2px solid #E9E0DC !important;
            border-radius: 10px !important;
            padding: 10px 25px !important;
        }

        div[data-testid="stVerticalBlockBorderWrapper"] {
            border-color: #D9A7B0;
        }

        /* Dividers */
        hr {
            border-color: #E3D8D3;
        }

        /* Mobile layout */
        @media (max-width: 768px) {
            .block-container {
                padding-left: 1rem;
                padding-right: 1rem;
            }
        }
    </style>    
    """, unsafe_allow_html=True)