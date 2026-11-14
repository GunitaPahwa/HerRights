import streamlit as st

def show_support():
    st.title("Help & Support")

    st.write(
        "Find emergency contacts. free legal assistance, and official "
        "resources for women's safety and rights in India."
    )
    st.subheader("🚨 Emergency & Helpline Numbers")
    st.error("If you are in immediate danger, call 112.")
    st.markdown("""
        - **112** - National Emergency Response
        - **181** - Women Helpline (availability may vary by state)
        - **1930** - Cybercrime and Online Financial Fraud Helpline
        - **1098** - Child Helpline
    """)

    st.subheader("⚖️ Free Legal Aid")
    st.write(
        "Women can seek free legal assistance through the National "
        "Legal Services Authority (NALSA), District Legal Services "
        "Authorities, and legal aid clinics."
    )
    st.markdown("""
        - **Legal Aid Helpline:** 15100
        - **NALSA Website:** https://nalsa.gov.in/
    """)

    st.subheader("🌐 Official Complaint & Support Portals")
    st.markdown("""
        **1. National Commission for Women (NCW)**
        For women's rights complaints and grievance assistance.
        https://ncw.gov.in/

        **2. SHe-Box Portal**
        For workplace sexual harassment complaints.
        https://shebox.wcd.gov.in/

        **3. National Cyber Crime Reporting Portal**
        For reporting cyber harassment, online abuse, and cybercrime.
        https://cybercrime.gov.in/

        **4. Mission Shakti**
        For information about women's support services, including One Stop Centres.
        https://missionshakti.wcd.gov.in/
    """)

    st.subheader("🛡️ Basic Safety Guidance")
    st.markdown("""
        - If you are in immediate danger, contact emergency services.
        - Reach out to a tursted person when it is safe to do so.
        - Preserve relevant messages, documntes, or other evidence safely.
        - Seek medical assistance if you have been injured.
        - Contact a legal aid service or appropriate authority for guidance.
        - If your device is being monitored, use a safer device to seek help.
    """)

    st.subheader("Important Disclaimer")
    st.info(
        "HerRights provides general legal information and awareness "
        "resources. It does not replace professional legal advice, "
        "emergency assistance, or official complaint procedures. Helpline "
        "availability and services may vary."
    )