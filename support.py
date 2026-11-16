import streamlit as st

def show_support():
    st.title("Help & Support")

    st.write(
        "Find emergency contacts. free legal assistance, and official "
        "resources for women's safety and rights in India."
    )
    st.subheader("🚨 Emergency & Helpline Numbers")
    st.markdown("""
        <div class="support-emergency">
            <div class="support-emergency-title">
                ⚠ In immediate danger? Call 112
            </div>
            <div class="support-emergency-desc">
                India's national emergency response number.
            </div>
        </div>
    """, unsafe_allow_html=True)
    helplines = [
        ("112", "National Emergency"),
        ("181", "Women Helpline"),
        ("1930", "Cybercrime Helpline"),
        ("1098", "Child Helpline")
    ]
    for start in range(0, len(helplines), 2):
        cols = st.columns(2, gap="small")
        for col, (number, label) in zip(cols, helplines[start:start + 2]):
            with col:
                st.markdown(
                    f"""
                    <div class="support-helpline-card">
                        <div class="support-helpline-number">{number}</div>
                        <div class="support-helpline-label">{label}</div>
                    </div>
                    """, unsafe_allow_html=True
                )

    st.subheader("⚖️ Free Legal Aid")
    st.markdown("""
        <div class="support-legal-card">
            <div class="support-legal-title">
                National Legal Services Authority (NALSA)
            </div>
            <p class="support-legal-desc">
                Free legal assistance through NALSA, Distric Legal Services Authorities and legal aid clinics.
            </p>
            <div class="support-legal-footer">
                <span class="support-legal-phone">☎ &nbsp;15100</span>
                <a href="https://nalsa.gov.in/" target="_blank" rel="noopener noreferrer">
                    Visit NALSA ↗
                </a>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.subheader("🌐 Official Complaint & Support Portals")
    portals = [
       (
            "National Commission for Women (NCW)",
            "Women's rights complaints and grievance assistance.",
            "https://ncw.gov.in/",
            "Visit NCW"
        ),
        (
            "SHe-Box Portal",
            "Workplace sexual harassment complaints.",
            "https://shebox.wcd.gov.in/",
            "Visit SHe-Box"
        ),
        (
            "National Cyber Crime Reporting Portal",
            "Report cyber harassment, online abuse, and cybercrime.",
            "https://cybercrime.gov.in/",
            "Visit Portal"
        ),
        (
            "Mission Shakti",
            "Women's support services, and One Stop Centres.",
            "https://missionshakti.wcd.gov.in/",
            "Visit Portal"
        )
    ]
    for row_start in range(0, len(portals), 2):
        cols = st.columns(2, gap="medium")
        for col, (title, desc, url, link_text) in zip(cols, portals[row_start:row_start + 2]):
            with col:
                st.markdown(
                    f"""
                    <div class="support-portal-card">
                        <div class="support-portal-title">{title}</div>
                        <div class="support-portal-desc">{desc}</div>
                        <a href="{url}" target="_blank" rel="noopener noreferrer">
                            {link_text} ↗
                        </a>
                    </div>
                    """, unsafe_allow_html=True
                )

    st.subheader("🛡️ Basic Safety Guidance")
    st.markdown("""
        <div class="support-safety-list">
            <div class="support-safety-item">
                <span class="support-safety-check">✓</span>
                If you are in immediate danger, contact emergency services.
            </div> 
            <div class="support-safety-item">
                <span class="support-safety-check">✓</span>
                Reach out to a trusted person when it is safe to do so.
            </div>
            <div class="support-safety-item">
                <span class="support-safety-check">✓</span>
                Preserve relevant messages, documntes, or other evidence safely.
            </div>
            <div class="support-safety-item">
                <span class="support-safety-check">✓</span>
                Seek medical assistance if you have been injured.
            </div>
            <div class="support-safety-item">
                <span class="support-safety-check">✓</span>
                Contact a legal aid service or appropriate authority for guidance.
            </div>
            <div class="support-safety-item">
                <span class="support-safety-check">✓</span>
                If your device is being monitored, use a safer device to seek help.
            </div>
        </div>
    """,unsafe_allow_html=True)

    st.subheader("Important Disclaimer")
    st.info(
        "HerRights provides general legal information and awareness "
        "resources. It does not replace professional legal advice, "
        "emergency assistance, or official complaint procedures. Helpline "
        "availability and services may vary."
    )