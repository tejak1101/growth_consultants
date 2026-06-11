import streamlit as st
from pathlib import Path
import json, os

st.set_page_config(
    page_title="Growth Consultants",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Load CSS ──────────────────────────────────────────────────────────────────
def load_css():
    css_path = Path(__file__).parent / "assets" / "style.css"
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# ── Sidebar navigation ────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class="sidebar-brand">
        <span class="brand-icon">🚀</span>
        <div>
            <div class="brand-name">Growth Consultants</div>
            <div class="brand-sub">Business OS</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='nav-divider'></div>", unsafe_allow_html=True)

    pages = {
        "🏠  Dashboard":       "dashboard",
        "✅  Project Tracker": "tracker",
        "👥  Clients":         "clients",
        "📋  Onboarding":      "onboarding",
        "🔧  Tools & Stack":   "tools",
    }

    if "page" not in st.session_state:
        st.session_state.page = "dashboard"

    for label, key in pages.items():
        active = "nav-active" if st.session_state.page == key else ""
        if st.button(label, key=f"nav_{key}", use_container_width=True):
            st.session_state.page = key
            st.rerun()

    st.markdown("<div class='nav-divider'></div>", unsafe_allow_html=True)
    st.markdown("<div class='sidebar-footer'>Growth Consultants © 2026</div>", unsafe_allow_html=True)

# ── Page routing ──────────────────────────────────────────────────────────────
page = st.session_state.page

if page == "dashboard":
    from pages import dashboard; dashboard.render()
elif page == "tracker":
    from pages import tracker; tracker.render()
elif page == "clients":
    from pages import clients; clients.render()
elif page == "onboarding":
    from pages import onboarding; onboarding.render()
elif page == "tools":
    from pages import tools; tools.render()
