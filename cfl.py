import base64
from pathlib import Path

import streamlit as st

INTRO_LOGO_PATH = Path(__file__).resolve().parent / "intro_logo.jpg"

# Page Configuration
st.set_page_config(
    page_title="The Care for Life Foundation",
    page_icon="💜",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling & Theme (Deep Purple & Clean Accents)
st.markdown("""
    <style>
    .main {
        background-color: #0b071e;
        color: #e0e0e0;
    }
    .hero-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #ffffff;
        text-align: center;
        letter-spacing: 2px;
    }
    .hero-subtitle {
        font-size: 1.2rem;
        color: #b19cd9;
        text-align: center;
        margin-bottom: 30px;
    }
    .card {
        background-color: #140d2f;
        padding: 25px;
        border-radius: 12px;
        border: 1px solid #2a1b54;
        margin-bottom: 20px;
    }
    @keyframes intro-logo-fade {
        0%, 15% { opacity: 0; }
        35%, 65% { opacity: 1; }
        100% { opacity: 0; }
    }
    @keyframes intro-overlay-dismiss {
        0%, 65% { opacity: 1; }
        100% { opacity: 0; visibility: hidden; }
    }
    .intro-overlay {
        position: fixed;
        inset: 0;
        z-index: 999999;
        display: flex;
        align-items: center;
        justify-content: center;
        background: #0b071e;
        pointer-events: none;
        animation: intro-overlay-dismiss 3s ease-in-out forwards;
    }
    .intro-overlay img {
        max-width: 90vw;
        max-height: 90vh;
        object-fit: contain;
        animation: intro-logo-fade 3s ease-in-out forwards;
    }
    </style>
""", unsafe_allow_html=True)

# Session State for Intro Screen Toggle
if 'entered' not in st.session_state:
    st.session_state.entered = False
if 'intro_animation_shown' not in st.session_state:
    st.session_state.intro_animation_shown = False

if not st.session_state.entered:
    # --- INTRO / SPLASH SCREEN ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h1 class='hero-title'>THE CARE FOR LIFE FOUNDATION</h1>", unsafe_allow_html=True)
    st.markdown("<p class='hero-subtitle'>You are loved &bull; Life &bull; Health &bull; Welfare</p>", unsafe_allow_html=True)

    if st.button("Enter Foundation Portal", use_container_width=True, type="primary"):
        st.session_state.entered = True
        st.rerun()

else:
    # --- MAIN WEBSITE DASHBOARD ---
    if not st.session_state.intro_animation_shown:
        logo_data = base64.b64encode(INTRO_LOGO_PATH.read_bytes()).decode("ascii")
        st.markdown(
            "<div class='intro-overlay'>"
            f"<img src='data:image/jpeg;base64,{logo_data}' alt='Care for Life Foundation logo'>"
            "</div>",
            unsafe_allow_html=True,
        )
        st.session_state.intro_animation_shown = True
    
    # Sidebar Navigation
    st.sidebar.title("Navigation")
    menu = st.sidebar.radio("Go to:", ["Home & Mission", "Our Initiatives", "Get Involved"])
    
    if menu == "Home & Mission":
        st.markdown("<h1 class='hero-title'>Empowering Lives & Communities</h1>", unsafe_allow_html=True)
        st.markdown("<p class='hero-subtitle'>Dedicated to general human welfare, health advocacy, and community support.</p>", unsafe_allow_html=True)
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
                <div class='card'>
                    <h3>🌟 Our Core Vision</h3>
                    <p>We believe in holistic human welfare—moving beyond basic material aid to tackle community health education, medical security, and youth empowerment from the ground up.</p>
                </div>
            """, unsafe_allow_html=True)
            
        with col2:
            st.markdown("""
                <div class='card'>
                    <h3>💡 What We Do</h3>
                    <p>We organize community health outreaches and support practical initiatives that strengthen health, welfare, and youth empowerment.</p>
                </div>
            """, unsafe_allow_html=True)

    elif menu == "Our Initiatives":
        st.markdown("# 🚀 Core Initiatives")
        st.write("Explore the active programs and technological solutions driven by the Care for Life Foundation.")
        
        st.markdown("""
        <div class='card'>
            <h4>1. Community Health & Welfare Outreaches</h4>
            <p>Direct grassroots engagement providing health education, basic medical support, and welfare advocacy to under-resourced communities.</p>
        </div>
        
        <div class='card'>
            <h4>2. Youth Advocacy & Development</h4>
            <p>Empowering young minds through mentorship, leadership training, and collaborative community projects.</p>
        </div>
        """, unsafe_allow_html=True)

    elif menu == "Get Involved":
        st.markdown("# 🤝 Join Our Mission")
        st.write("Whether you want to volunteer, partner on health outreaches, or support our welfare initiatives, we'd love to hear from you.")
        st.markdown(
            "[WhatsApp: +234 8038615766](https://wa.me/2348038615766) · "
            "[Email: cflfoundation12@gmail.com](mailto:cflfoundation12@gmail.com)"
        )
        
        with st.form("contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Email Address")
            message = st.text_input("How would you like to get involved?")
            submitted = st.form_submit_button("Send Message")
            if submitted:
                st.success("Thank you! Your message has been recorded. We will reach out soon.")