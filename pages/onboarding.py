import streamlit as st
from pages.data_store import get_check, set_check, load_checklist, save_checklist

ONBOARDING_STEPS = [
    {
        "phase": "Phase 1 — Foundation",
        "steps": [
            {
                "num": 1, "title": "Discord Server Setup",
                "desc": "Buat Discord server dan setup semua channel yang diperlukan untuk manage bisnis.",
                "status": "done",
                "checklist": [
                    "Buat server Discord baru",
                    "Buat semua kategori (Text Channels, Sales, Client Assets, Team, Low Ticket)",
                    "Buat semua channel dengan emoji",
                    "Grant admin access ke Teja",
                ],
                "defaults": [True, True, True, True],
                "tools": ["Discord"],
                "ref": "Video: Setting Up Discord for Client Management"
            },
            {
                "num": 2, "title": "Zapier Automations",
                "desc": "Hubungkan semua tools ke Discord agar notifikasi masuk otomatis.",
                "status": "next",
                "checklist": [
                    "Buat akun Zapier",
                    "Connect Typeform → #typeform-submissions",
                    "Connect GHL Calendar (booked calls) → #booked-calls",
                    "Connect Stripe/Whop → #payments",
                    "Setup EOD reminder di #eods",
                ],
                "defaults": [False, False, False, False, False],
                "tools": ["Zapier", "Discord"],
                "ref": "Video: Setting Up Discord Automations"
            },
            {
                "num": 3, "title": "Email Service Provider (Kit)",
                "desc": "Setup ConvertKit untuk email marketing dan broadcast ke leads.",
                "status": "pending",
                "checklist": [
                    "Buat akun di kit.com",
                    "Setup email templates",
                    "Buat ConvertKit Zap di Zapier",
                ],
                "defaults": [False, False, False],
                "tools": ["Kit / ConvertKit", "Zapier"],
                "ref": "Video: Setting Up Your Email Service Provider"
            },
            {
                "num": 4, "title": "CRM — GoHighLevel",
                "desc": "Setup CRM untuk manage pipeline klien dan automation.",
                "status": "pending",
                "checklist": [
                    "Login ke gohighlevel.com",
                    "Connect calendar",
                    "Setup client pipeline",
                    "Konfigurasi tags dan automations",
                    "Update DQ path (DQ102): tambah 3-5K",
                ],
                "defaults": [False, False, False, False, False],
                "tools": ["GoHighLevel"],
                "ref": "Video: GoHighLevel CRM Walkthrough"
            },
            {
                "num": 5, "title": "Typeform Application",
                "desc": "Buat form aplikasi dengan logika kualifikasi leads.",
                "status": "pending",
                "checklist": [
                    "Buat akun Typeform di typeform.com",
                    "Build application form dengan qualification questions",
                    "Set DQ logic: <3K dan 3-5K = disqualified",
                    "Connect Typeform ke Zapier",
                    "Connect Typeform ke GHL",
                ],
                "defaults": [False, False, False, False, False],
                "tools": ["Typeform", "Zapier", "GoHighLevel"],
                "ref": "Video: T5 Typeform Application Process"
            },
            {
                "num": 6, "title": "Payment Processor",
                "desc": "Setup Stripe untuk menerima pembayaran dan connect ke Zapier.",
                "status": "pending",
                "checklist": [
                    "Buat akun Stripe",
                    "Setup Whop (opsional)",
                    "Connect payment processor ke Zapier",
                    "Test payment notification ke #payments Discord",
                ],
                "defaults": [False, False, False, False],
                "tools": ["Stripe", "Whop", "Zapier"],
                "ref": "Video: Understanding Payments Tracking"
            },
        ]
    },
    {
        "phase": "Phase 2 — Client System",
        "steps": [
            {
                "num": 7, "title": "Client Onboarding Process",
                "desc": "Buat sistem onboarding terstruktur untuk klien baru.",
                "status": "pending",
                "checklist": [
                    "Buat onboarding document untuk klien baru",
                    "Setup onboarding flow di GHL",
                    "Buat welcome sequence di ConvertKit",
                    "Pin onboarding resources di #onboarding Discord",
                ],
                "defaults": [False, False, False, False],
                "tools": ["GHL", "Discord", "ConvertKit"],
                "ref": "Doc: CO1 Full Onboarding Document"
            },
            {
                "num": 8, "title": "Sales System & Scripts",
                "desc": "Setup tools dan scripts untuk tim sales.",
                "status": "pending",
                "checklist": [
                    "Buat setter tracking sheet",
                    "Buat closing script dari offer",
                    "Setup closer tracking sheet",
                    "Buat UTM links untuk setters",
                    "Setup daily team call schedule",
                ],
                "defaults": [False, False, False, False, False],
                "tools": ["Google Sheets", "Docs"],
                "ref": "Template: CO1 2-Step Close Template"
            },
            {
                "num": 9, "title": "Freebie & Lead Magnet",
                "desc": "Buat freebie berkualitas tinggi untuk lead generation.",
                "status": "pending",
                "checklist": [
                    "Design freebie (PDF atau video)",
                    "Connect freebie ke email opt-in funnel",
                    "Setup 14-day launch sequence di IG stories",
                    "Setup weekly promo schedule",
                ],
                "defaults": [False, False, False, False],
                "tools": ["Canva", "Kit", "Instagram"],
                "ref": "Video: Creating High-Value Freebies for Success"
            },
        ]
    },
    {
        "phase": "Phase 3 — Scale",
        "steps": [
            {
                "num": 10, "title": "Facebook Ads untuk Bisnis Sendiri",
                "desc": "Launch FB Ads untuk generate leads bisnis sendiri.",
                "status": "pending",
                "checklist": [
                    "Setup Meta Business Manager",
                    "Buat ad creative dan copy",
                    "Launch campaign pertama",
                    "Optimize berdasarkan data",
                ],
                "defaults": [False, False, False, False],
                "tools": ["Meta Ads Manager", "GoHighLevel"],
                "ref": "Video: Automating Ads for Better Conversions"
            },
            {
                "num": 11, "title": "Low-Ticket Funnel",
                "desc": "Build low-ticket offer untuk upsell dari leads yang masuk.",
                "status": "pending",
                "checklist": [
                    "Define low-ticket offer",
                    "Setup #low-ticket-lead Discord channel (sudah ada)",
                    "Build funnel di GHL",
                    "Connect ke Zapier",
                ],
                "defaults": [False, False, False, False],
                "tools": ["GHL", "Whop", "Discord"],
                "ref": None
            },
            {
                "num": 12, "title": "ManyChat Automation",
                "desc": "Automasi IG/FB DM untuk convert followers jadi leads.",
                "status": "pending",
                "checklist": [
                    "Buat akun ManyChat",
                    "Connect ke Instagram",
                    "Buat keyword triggers",
                    "Connect ke Typeform atau GHL",
                ],
                "defaults": [False, False, False, False],
                "tools": ["ManyChat", "Instagram"],
                "ref": None
            },
        ]
    },
]

STATUS_BADGE_MAP = {
    "done":    '<span class="phase-badge phase-done">✅ Done</span>',
    "next":    '<span class="phase-badge phase-next">🔄 Next</span>',
    "pending": '<span class="phase-badge phase-pending">⏳ Pending</span>',
}

def auto_status(step_num, total, done_count):
    """Auto-derive status badge from checklist progress."""
    if done_count == total:
        return "done"
    elif done_count > 0:
        return "next"
    else:
        return "pending"

def render():
    st.markdown("""
    <div class="page-header">
        <div class="page-eyebrow">SETUP GUIDE</div>
        <div class="page-title">Onboarding Steps</div>
        <div class="page-sub">Panduan lengkap setup semua sistem Growth Consultants — centang item saat selesai</div>
    </div>
    """, unsafe_allow_html=True)

    # ── Overall checklist progress ────────────────────────────────────────────
    all_items = sum(len(s["checklist"]) for sec in ONBOARDING_STEPS for s in sec["steps"])
    all_done  = sum(
        1 for sec in ONBOARDING_STEPS for s in sec["steps"]
        for i in range(len(s["checklist"]))
        if get_check(s["num"], i, s["defaults"][i])
    )
    overall_pct = int((all_done / all_items) * 100) if all_items else 0

    st.markdown(f"""
    <div class="section-card">
        <div class="section-card-title">📊 Overall Checklist Progress</div>
        <div class="progress-wrap">
            <div class="progress-label">
                <span>Total Items Selesai</span>
                <span style="color:#FFFFFF;font-weight:600">{overall_pct}% ({all_done}/{all_items})</span>
            </div>
            <div class="progress-bar-bg">
                <div class="progress-bar-fill" style="width:{overall_pct}%"></div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Steps per phase ───────────────────────────────────────────────────────
    for section in ONBOARDING_STEPS:
        st.markdown(f"""
        <div style="font-family:'Sora',sans-serif;font-size:18px;font-weight:700;
             color:#FFFFFF;margin:32px 0 16px;padding-bottom:10px;
             border-bottom:1px solid #1E1E2E">
            {section['phase']}
        </div>
        """, unsafe_allow_html=True)

        for step in section["steps"]:
            num   = step["num"]
            items = step["checklist"]
            total = len(items)

            # Load saved state for each item
            checked_states = [get_check(num, i, step["defaults"][i]) for i in range(total)]
            done_count = sum(checked_states)

            # Auto status based on progress
            status = auto_status(num, total, done_count)
            badge  = STATUS_BADGE_MAP[status]

            expander_label = f"Step {num}: {step['title']}  ·  {done_count}/{total} selesai"

            with st.expander(expander_label, expanded=(status == "next")):
                col_main, col_side = st.columns([3, 1])

                with col_main:
                    st.markdown(f"<p style='color:#C8C8E0;font-size:14px;margin-bottom:16px'>{step['desc']}</p>", unsafe_allow_html=True)
                    st.markdown("**Checklist:**")

                    # Render interactive checkboxes
                    for i, item_text in enumerate(items):
                        current = checked_states[i]
                        new_val = st.checkbox(
                            item_text,
                            value=current,
                            key=f"chk_{num}_{i}"
                        )
                        if new_val != current:
                            set_check(num, i, new_val)
                            st.rerun()

                    if step.get("ref"):
                        st.markdown(
                            f"<div style='margin-top:14px;font-size:12px;color:#6C63FF'>📖 Referensi: {step['ref']}</div>",
                            unsafe_allow_html=True
                        )

                with col_side:
                    st.markdown(badge, unsafe_allow_html=True)

                    # Mini progress bar
                    pct = int((done_count / total) * 100) if total else 0
                    st.markdown(f"""
                    <div style="margin-top:14px">
                        <div style="font-size:11px;color:#6B6B8A;margin-bottom:6px">Progress</div>
                        <div class="progress-bar-bg">
                            <div class="progress-bar-fill" style="width:{pct}%"></div>
                        </div>
                        <div style="font-size:11px;color:#6B6B8A;margin-top:4px;text-align:right">{pct}%</div>
                    </div>
                    """, unsafe_allow_html=True)

                    st.markdown("<br>", unsafe_allow_html=True)
                    st.markdown("**Tools:**")
                    for tool in step["tools"]:
                        st.markdown(f"<div style='font-size:12px;color:#818CF8;padding:2px 0'>🔧 {tool}</div>", unsafe_allow_html=True)

                    # Reset button for this step
                    if done_count > 0:
                        if st.button("↺ Reset", key=f"reset_{num}"):
                            data = {}
                            from pages.data_store import load_checklist
                            data = load_checklist()
                            for i in range(total):
                                data[f"step_{num}_item_{i}"] = False
                            from pages.data_store import save_checklist
                            save_checklist(data)
                            st.rerun()
