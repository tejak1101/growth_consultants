import streamlit as st
from pages.data_store import load_clients, add_client, update_client, delete_client

STATUS_COLOR = {"Active": "#4ADE80", "Onboarding": "#FCD34D", "Paused": "#F87171", "Completed": "#818CF8"}

def render():
    st.markdown("""
    <div class="page-header">
        <div class="page-eyebrow">CRM LITE</div>
        <div class="page-title">Clients</div>
        <div class="page-sub">Manage semua klien Growth Consultants</div>
    </div>
    """, unsafe_allow_html=True)

    clients = load_clients()

    # ── Stats row ────────────────────────────────────────────────────────────
    total    = len(clients)
    active   = sum(1 for c in clients if c["status"] == "Active")
    boarding = sum(1 for c in clients if c["status"] == "Onboarding")

    st.markdown(f"""
    <div class="metric-grid" style="grid-template-columns:repeat(3,1fr)">
        <div class="metric-card" style="--accent:#4ADE80">
            <div class="metric-icon">👥</div>
            <div class="metric-value">{total}</div>
            <div class="metric-label">Total Clients</div>
        </div>
        <div class="metric-card" style="--accent:#6C63FF">
            <div class="metric-icon">✅</div>
            <div class="metric-value">{active}</div>
            <div class="metric-label">Active</div>
        </div>
        <div class="metric-card" style="--accent:#FCD34D">
            <div class="metric-icon">🚀</div>
            <div class="metric-value">{boarding}</div>
            <div class="metric-label">Onboarding</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Client cards ─────────────────────────────────────────────────────────
    if not clients:
        st.info("Belum ada klien. Tambahkan klien pertama di bawah!")
    else:
        for c in clients:
            sc = STATUS_COLOR.get(c["status"], "#6B6B8A")
            col_card, col_actions = st.columns([5, 1])

            with col_card:
                st.markdown(f"""
                <div class="client-card">
                    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:12px">
                        <div class="client-name">{c['name']}</div>
                        <span style="font-size:12px;font-weight:600;color:{sc};
                            background:{'#0D2A1A' if c['status']=='Active' else '#2A1F00'};
                            padding:4px 12px;border-radius:20px;border:1px solid {sc}40">
                            ● {c['status']}
                        </span>
                    </div>
                    <div class="client-detail">🏢 {c.get('business','—')}</div>
                    <div class="client-detail">🎯 Funnel: {c.get('funnel_type','—')}</div>
                    <div class="client-detail">💰 Monthly Revenue: ${c.get('monthly_revenue','—')}</div>
                    <div class="client-detail">📅 Start: {c.get('start_date','—')}</div>
                    <div class="client-detail">🔧 Platforms: {c.get('platforms','—')}</div>
                    {"<div class='client-detail' style='margin-top:10px;color:#C8C8E0'>📝 " + c['notes'] + "</div>" if c.get('notes') else ""}
                </div>
                """, unsafe_allow_html=True)

            with col_actions:
                st.markdown("<br><br>", unsafe_allow_html=True)
                if st.button("✏️ Edit", key=f"edit_c_{c['id']}"):
                    st.session_state[f"edit_client_{c['id']}"] = True

            # Inline edit
            if st.session_state.get(f"edit_client_{c['id']}"):
                with st.form(key=f"form_c_{c['id']}"):
                    st.markdown(f"**Edit: {c['name']}**")
                    col1, col2 = st.columns(2)
                    with col1:
                        e_name     = st.text_input("Nama",     value=c["name"])
                        e_business = st.text_input("Business", value=c.get("business",""))
                        e_funnel   = st.selectbox("Funnel Type", ["VSL Funnel","Webinar Funnel","Direct Offer","Other"],
                                                  index=["VSL Funnel","Webinar Funnel","Direct Offer","Other"].index(c.get("funnel_type","Other")))
                        e_revenue  = st.text_input("Monthly Revenue ($)", value=c.get("monthly_revenue",""))
                    with col2:
                        e_status    = st.selectbox("Status", ["Active","Onboarding","Paused","Completed"],
                                                   index=["Active","Onboarding","Paused","Completed"].index(c.get("status","Active")))
                        e_start     = st.text_input("Start Date", value=c.get("start_date",""))
                        e_platforms = st.text_input("Platforms", value=c.get("platforms",""))
                        e_notes     = st.text_area("Notes", value=c.get("notes",""), height=100)

                    c1, c2, c3 = st.columns(3)
                    with c1: save_b   = st.form_submit_button("💾 Simpan")
                    with c2: delete_b = st.form_submit_button("🗑️ Hapus")
                    with c3: cancel_b = st.form_submit_button("✕ Cancel")

                    if save_b:
                        update_client(c["id"], {
                            "name": e_name, "business": e_business, "funnel_type": e_funnel,
                            "monthly_revenue": e_revenue, "status": e_status,
                            "start_date": e_start, "platforms": e_platforms, "notes": e_notes
                        })
                        st.session_state[f"edit_client_{c['id']}"] = False
                        st.rerun()
                    if delete_b:
                        delete_client(c["id"])
                        st.session_state[f"edit_client_{c['id']}"] = False
                        st.rerun()
                    if cancel_b:
                        st.session_state[f"edit_client_{c['id']}"] = False
                        st.rerun()

    # ── Add Client ───────────────────────────────────────────────────────────
    st.markdown("<br>", unsafe_allow_html=True)
    with st.expander("➕  Tambah Klien Baru"):
        with st.form("add_client_form"):
            st.markdown("**Klien Baru**")
            col1, col2 = st.columns(2)
            with col1:
                n_name     = st.text_input("Nama Klien *")
                n_business = st.text_input("Business / Niche")
                n_funnel   = st.selectbox("Funnel Type", ["VSL Funnel","Webinar Funnel","Direct Offer","Other"])
                n_revenue  = st.text_input("Monthly Revenue ($)")
            with col2:
                n_status    = st.selectbox("Status", ["Onboarding","Active","Paused","Completed"])
                n_start     = st.text_input("Start Date (YYYY-MM-DD)")
                n_platforms = st.text_input("Platforms (cth: Facebook Ads, GHL)")
                n_notes     = st.text_area("Notes", height=80)

            if st.form_submit_button("➕ Tambah Klien", use_container_width=True):
                if n_name.strip():
                    add_client({
                        "name": n_name.strip(), "business": n_business,
                        "funnel_type": n_funnel, "monthly_revenue": n_revenue,
                        "status": n_status, "start_date": n_start,
                        "platforms": n_platforms, "notes": n_notes,
                    })
                    st.success(f"Klien '{n_name}' berhasil ditambahkan!")
                    st.rerun()
                else:
                    st.error("Nama klien tidak boleh kosong.")
