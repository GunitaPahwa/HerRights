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
            color: #F1E9E5;
            border-radius: 12px;
            border: none;
            padding: 10px 24px;
        }

        div.stButton > button p {
            color: #F1E9E5;
        }

        div.stButton > button:hover {
            background-color: #87AA94;
            color: #342D30;
        }

        div.stButton > button:hover p {
            color: #342D30;
        }

        /* info boxes */
        div[data-testid="stAlert"] > div {
            background-color: #F8E8EA !important;
            border-radius: 10px !important;
            border-left: 4px solid #A66B7E !important;
        }

        div[data-testid="stAlert"] p {
            color: #702F46 !important;
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

        /* Explore rights page */
        [class*="st-key-rights_card_"] {
            border-left: 6px solid #87AA94 !important;
            border-radius: 14px !important;
        }

        div.stLinkButton > a {
            border-radius: 7px !important;
            border: 2px solid #87AA94 !important;
            padding: 0 8px 0 8px !important;
        }

        div.stLinkButton > a:hover {
            background-color: #A9C5B3 !important;
            border: 2px solid #87AA94 !important;
        }

        /* Guidance page */
        div[data-testid="stTextArea"] textarea {
            border-radius: 10px !important;
            border: 1px solid #A9C5B3 !important;
        }

        div[data-testid="stTextArea"] textarea:focus {
            border-color: #456B5A !important;
        }

        .guidance-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
            margin: 12px 0 20px;
        }

        .guidance-tag {
            display: inline-block;
            background-color: #EEE6E1;
            color: #702F46;
            border: 1px solid #D9C9CB;
            border-radius: 20px;
            padding: 9px 16px;
            font-size: 15px;
            font-weight: 500;
        }

        [class*="st-key-guidance_right_"] {
            border-left: 6px solid #87AA94 !important;
            border-radius: 12px !important;
        }

        .st-key-get_guidance_btn button, .st-key-guidance_complaint button, .st-key-download_complaint button {
            background-color: #7F9F8D !important;
            border: 1px solid #628574 !important;
            border-radius: 8px !important;
            padding: 12px 30px !important;

        }

        .st-key-get_guidance_btn button p, .st-key-guidance_complaint button p, .st-key-download_complaint button p {
            color: black !important;
            font-size: 15px;
            font-weight: 500 !important;
        }

        .st-key-get_guidance_btn button:hover, .st-key-guidance_complaint button:hover, .st-key-download_complaint button:hover {
            background-color: #A1B9AA !important;
            color: #702F46 !important;
            # border-color: #628574 !important;
        }

        .guidance-question {
            background-color: #E7EFE8;
            border-left: 4px solid #87AA94;
            border-radius: 10px;
            padding: 16px 20px;
            color: #342D30;
            line-height: 1.6;
            margin: 2px 0 12px;
        }

        /* complaint generator page */
        .st-key-submission_card {
            border: 1px solid #D6D1C9;
            border-left: 6px solid #87AA94;
            border-radius: 14px;
            padding: 20px 24px;
            margin: 12px 0 24px;
        }
        
        .submission-content {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .submission-section {
            margin-top: -7px;
            display: flex;
            flex-direction: column;
            gap: 3px;
        }

        .submission-label {
            color: #702F46;
            font-weight: 650;
            font-size: 16px;
        }

        .submission-section p, .sumbission-important p {
            margin: 0;
            color: #342D30;
            line-height: 1.7;
        }

        .submission-separator {
            height: 1px;
            background-color: #DDD8D0;
            margin-bottom: 10px;
        }

        .submission-important {
            background-color: #F8E8EA;
            border-radius: 10px;
            padding: 10px 20px 0;
            # display: flex;
            flex-direction: column;
            gap: 6px;
            margin: 0 0 7px 0;
            font-size: 15px;
        }

        .submission-important strong {
            color: #702F46;
            font-weight: 650;
            font-size: 15px;            
        }

        /* help and support page */
        .support-emergency {
            background-color: #F8E8EA;
            border-radius: 10px;
            padding: 16px;
            margin-bottom: 14px;
        }

        .support-emergency-title, .support-legal-title {
            color: #702F46;
            font-weight: 700;
            font-size: 17px;
            margin-bottom: 5px;
        }

        .support-helpline-desc {
            color: #702F46;
            font-size: 14px;
        }

        .support-helpline-card, .support-legal-card, .support-portal-card {
            border: 2px solid #D6D1C9;
            border-radius: 10px;
            padding: 10px 16px;
            min-height: 90px;
            margin-bottom: 13px;
        }

        .support-helpline-number {
            font-family: Georgia, serif;
            font-size: 27px;
            font-weight: bold;
            color: #702F46;
            margin-bottom: 3px;
        }

        .support-helpline-label {
            font-size: 15px;
            color: #342D30;
        }

        .support-legal-title {
            margin-top: 5px;
        }

        .support-legal-desc, .support-portal-desc {
            color: #342D30;
            font-size: 15px;
            margin: 12px 0 13px;
            line-height: 1.5;
        }

        .support-legal-footer {
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
        }

        .support-legal-footer a, .support-portal-card a  {
            color: #456B5A;
            font-weight: 500;
            text-decoration: none;
            margin-right: 60px;
        }

        .support-legal-footer a:hover, .support-portal-card a:hover {
            text-decoration: underline;
        }

        .support-legal-phone{
            color: #342D30;
            font-weight: 600;
        }

        .support-portal-title {
            font-family: Georgia, serif;
            font-size: 21px;
            font-weight: bold;
            color: #702F46;
            margin-bottom: -9px;
        }

        .support-portal-card {
            display: flex;
            flex-direction: column;
        }

        .support-portal-card a {
            margin-top: auto;
            align-self: flex-end;
        }

        .support-portal-desc {
            margin-bottom: 2px;
        }

        .support-portal-card a {
            margin-right: 10px;
        }

        .support-safety-list {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 14px 45px;
            margin-top: 10px;
            margin-bottom: 20px;
        }

        .support-safety-item {
            display: flex;
            align-items: flex-start;
            gap: 12px;
            font-size: 16px;
            color: #342D30;
            line-height: 1.5;
        }

        .support-safety-check {
            color: #456B5A;
            font-size: 20px;
            font-weight: bold;
            flex-shrink: 0;
        }

        /* Dividers */
        hr {
            border: none !important;
            height: 3px !important;
            background: linear-gradient(
                90deg,
                transparent 0%,
                #A66B7E 50%,
                transparent 100%
            ) !important;
            # background-color: #D9A7B0 !important;
            width: 80% !important;
            jsutify-content: center !important;
            margin: 30px auto !important;
            border-radius: 5px !important;
        }

        /* Mobile layout */
        @media (max-width: 768px) {
            .block-container {
                padding-left: 1rem;
                padding-right: 1rem;
            }

            .support-safety-list {
                grid-template-columns: 1fr;
            }
        }
    </style>    
    """, unsafe_allow_html=True)