import streamlit as st

TOOLS = [
    {"icon": "💬", "name": "Discord",         "purpose": "Team communication + automated notifications untuk booked calls, payments, dan typeform submissions.", "phase": "Phase 1 ✅", "url": "https://discord.com",         "status": "Active"},
    {"icon": "⚡", "name": "Zapier",           "purpose": "Menghubungkan semua tools dan mengotomatiskan workflows antar platform.", "phase": "Phase 1 🔄",  "url": "https://zapier.com",          "status": "Next"},
    {"icon": "📊", "name": "GoHighLevel",      "purpose": "CRM utama untuk manage pipeline klien, calendar booking, dan automations.", "phase": "Phase 1 ⏳",  "url": "https://gohighlevel.com",     "status": "Pending"},
    {"icon": "📋", "name": "Typeform",         "purpose": "Form aplikasi untuk kualifikasi leads. DQ logic: <3K dan 3-5K = disqualified.", "phase": "Phase 1 ⏳", "url": "https://typeform.com",         "status": "Pending"},
    {"icon": "📧", "name": "Kit (ConvertKit)", "purpose": "Email marketing, broadcast ke leads, dan nurture sequences.", "phase": "Phase 1 ⏳",  "url": "https://kit.com",             "status": "Pending"},
    {"icon": "💳", "name": "Stripe",           "purpose": "Payment processor utama. Notifikasi otomatis ke Discord #payments via Zapier.", "phase": "Phase 1 ⏳", "url": "https://stripe.com",          "status": "Pending"},
    {"icon": "🛍️", "name": "Whop",            "purpose": "Platform untuk low-ticket offers dan community. Alternatif payment processor.", "phase": "Phase 1 ⏳", "url": "https://whop.com",            "status": "Pending"},
    {"icon": "💬", "name": "ManyChat",         "purpose": "Automasi DM Instagram dan Facebook untuk convert followers jadi leads.", "phase": "Phase 3 ⏳",  "url": "https://manychat.com",        "status": "Pending"},
    {"icon": "📣", "name": "Meta Ads Manager", "purpose": "Platform untuk run Facebook Ads — traffic utama untuk generate leads baru.", "phase": "Phase 3 ⏳", "url": "https://business.facebook.com","status": "Pending"},
    {"icon": "📊", "name": "Google Sheets",    "purpose": "Setter tracking sheet, closer tracking sheet, dan laporan harian.", "phase": "Phase 2 ⏳",  "url": "https://sheets.google.com",   "status": "Pending"},
]

STATUS_COLOR = {
    "Active":  ("#4ADE80", "#0D2A1A"),
    "Next":    ("#FCD34D", "#2A1F00"),
    "Pending": ("#818CF8", "#1A1A2E"),
}

def render():
    st.markdown("""
    <div class="page-header">
        <div class="page-eyebrow">TECH STACK</div>
        <div class="page-title">Tools & Stack</div>
        <div class="page-sub">Semua tools yang digunakan untuk operasional Growth Consultants</div>
    </div>
    """, unsafe_allow_html=True)

    # ── Summary ──────────────────────────────────────────────────────────────
    active  = sum(1 for t in TOOLS if t["status"] == "Active")
    next_up = sum(1 for t in TOOLS if t["status"] == "Next")
    pending = sum(1 for t in TOOLS if t["status"] == "Pending")

    st.markdown(f"""
    <div class="metric-grid" style="grid-template-columns:repeat(3,1fr)">
        <div class="metric-card" style="--accent:#4ADE80">
            <div class="metric-icon">✅</div>
            <div class="metric-value">{active}</div>
            <div class="metric-label">Connected</div>
        </div>
        <div class="metric-card" style="--accent:#FCD34D">
            <div class="metric-icon">🔄</div>
            <div class="metric-value">{next_up}</div>
            <div class="metric-label">In Progress</div>
        </div>
        <div class="metric-card" style="--accent:#818CF8">
            <div class="metric-icon">⏳</div>
            <div class="metric-value">{pending}</div>
            <div class="metric-label">Not Setup</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Tool Cards Grid ───────────────────────────────────────────────────────
    cols = st.columns(3)
    for i, tool in enumerate(TOOLS):
        text_color, bg_color = STATUS_COLOR.get(tool["status"], ("#818CF8","#1A1A2E"))
        with cols[i % 3]:
            st.markdown(f"""
            <div class="tool-card">
                <div class="tool-icon">{tool['icon']}</div>
                <div class="tool-name">{tool['name']}</div>
                <div class="tool-purpose">{tool['purpose']}</div>
                <div style="margin-top:14px;display:flex;align-items:center;justify-content:space-between">
                    <div class="tool-phase">{tool['phase']}</div>
                    <span style="font-size:11px;font-weight:600;color:{text_color};
                        background:{bg_color};padding:3px 10px;border-radius:20px">
                        {tool['status']}
                    </span>
                </div>
                <div style="margin-top:12px">
                    <a href="{tool['url']}" target="_blank"
                       style="font-size:12px;color:#6C63FF;text-decoration:none;font-weight:500">
                        🔗 {tool['url'].replace('https://','').rstrip('/')}
                    </a>
                </div>
            </div>
            <br>
            """, unsafe_allow_html=True)

    # ── How it connects ────────────────────────────────────────────────────────
    st.markdown("""
    <div class="section-card" style="margin-top:8px">
        <div class="section-card-title">🔗 Bagaimana Tools Terhubung</div>
        <div class="funnel-wrap">
            <div class="funnel-step">
                <div class="funnel-step-icon">📋</div>
                <div class="funnel-step-label">Typeform</div>
                <div class="funnel-step-sub">Lead apply</div>
            </div>
            <div class="funnel-arrow">→</div>
            <div class="funnel-step">
                <div class="funnel-step-icon">⚡</div>
                <div class="funnel-step-label">Zapier</div>
                <div class="funnel-step-sub">Automasi</div>
            </div>
            <div class="funnel-arrow">→</div>
            <div class="funnel-step">
                <div class="funnel-step-icon">💬</div>
                <div class="funnel-step-label">Discord</div>
                <div class="funnel-step-sub">Notifikasi tim</div>
            </div>
            <div class="funnel-arrow">+</div>
            <div class="funnel-step">
                <div class="funnel-step-icon">📊</div>
                <div class="funnel-step-label">GoHighLevel</div>
                <div class="funnel-step-sub">CRM pipeline</div>
            </div>
            <div class="funnel-arrow">+</div>
            <div class="funnel-step">
                <div class="funnel-step-icon">📧</div>
                <div class="funnel-step-label">Kit</div>
                <div class="funnel-step-sub">Email nurture</div>
            </div>
            <div class="funnel-arrow">→</div>
            <div class="funnel-step">
                <div class="funnel-step-icon">💳</div>
                <div class="funnel-step-label">Stripe</div>
                <div class="funnel-step-sub">Payment</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
