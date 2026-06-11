import streamlit as st
from pages.data_store import load_tasks, load_clients

def render():
    tasks   = load_tasks()
    clients = load_clients()

    done    = sum(1 for t in tasks if t["status"] == "Done")
    next_up = sum(1 for t in tasks if t["status"] == "Next")
    pending = sum(1 for t in tasks if t["status"] == "Pending")
    total   = len(tasks)
    progress_pct = int((done / total) * 100) if total else 0

    active_clients = sum(1 for c in clients if c["status"] == "Active")

    # ── Header ──────────────────────────────────────────────────────────────
    st.markdown("""
    <div class="page-header">
        <div class="page-eyebrow">OVERVIEW</div>
        <div class="page-title">Dashboard</div>
        <div class="page-sub">Business OS untuk Growth Consultants</div>
    </div>
    """, unsafe_allow_html=True)

    # ── Metric Cards ─────────────────────────────────────────────────────────
    st.markdown(f"""
    <div class="metric-grid">
        <div class="metric-card" style="--accent:#4ADE80">
            <div class="metric-icon">✅</div>
            <div class="metric-value">{done}</div>
            <div class="metric-label">Tasks Done</div>
        </div>
        <div class="metric-card" style="--accent:#FCD34D">
            <div class="metric-icon">🔄</div>
            <div class="metric-value">{next_up}</div>
            <div class="metric-label">In Progress</div>
        </div>
        <div class="metric-card" style="--accent:#818CF8">
            <div class="metric-icon">⏳</div>
            <div class="metric-value">{pending}</div>
            <div class="metric-label">Pending</div>
        </div>
        <div class="metric-card" style="--accent:#F472B6">
            <div class="metric-icon">👥</div>
            <div class="metric-value">{active_clients}</div>
            <div class="metric-label">Active Clients</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Overall Progress ──────────────────────────────────────────────────────
    st.markdown(f"""
    <div class="section-card">
        <div class="section-card-title">📊 Overall Project Progress</div>
        <div class="progress-wrap">
            <div class="progress-label">
                <span>Setup Selesai</span>
                <span style="color:#FFFFFF;font-weight:600">{progress_pct}%</span>
            </div>
            <div class="progress-bar-bg">
                <div class="progress-bar-fill" style="width:{progress_pct}%"></div>
            </div>
        </div>
        <div style="font-size:12px;color:#6B6B8A;margin-top:8px">{done} dari {total} tasks selesai</div>
    </div>
    """, unsafe_allow_html=True)

    # ── Business Funnel ───────────────────────────────────────────────────────
    st.markdown("""
    <div class="section-card">
        <div class="section-card-title">🎯 Business Funnel</div>
        <div class="funnel-wrap">
            <div class="funnel-step">
                <div class="funnel-step-icon">📣</div>
                <div class="funnel-step-label">Traffic</div>
                <div class="funnel-step-sub">Facebook Ads / Organic</div>
            </div>
            <div class="funnel-arrow">→</div>
            <div class="funnel-step">
                <div class="funnel-step-icon">🎥</div>
                <div class="funnel-step-label">Conversion</div>
                <div class="funnel-step-sub">Webinar / VSL</div>
            </div>
            <div class="funnel-arrow">→</div>
            <div class="funnel-step">
                <div class="funnel-step-icon">📞</div>
                <div class="funnel-step-label">Sales</div>
                <div class="funnel-step-sub">Book a Call</div>
            </div>
            <div class="funnel-arrow">→</div>
            <div class="funnel-step">
                <div class="funnel-step-icon">🤝</div>
                <div class="funnel-step-label">Fulfilment</div>
                <div class="funnel-step-sub">Onboarding</div>
            </div>
            <div class="funnel-arrow">→</div>
            <div class="funnel-step">
                <div class="funnel-step-icon">🚀</div>
                <div class="funnel-step-label">Delivery</div>
                <div class="funnel-step-sub">Results</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Phase Progress ────────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-card-title'>📋 Phase Breakdown</div>", unsafe_allow_html=True)

    phases = ["Phase 1 — Foundation", "Phase 2 — Client System", "Phase 3 — Scale"]
    for phase in phases:
        phase_tasks = [t for t in tasks if t["phase"] == phase]
        phase_done  = sum(1 for t in phase_tasks if t["status"] == "Done")
        phase_total = len(phase_tasks)
        phase_pct   = int((phase_done / phase_total) * 100) if phase_total else 0

        st.markdown(f"""
        <div class="progress-wrap">
            <div class="progress-label">
                <span style="color:#C8C8E0;font-weight:500">{phase}</span>
                <span style="color:#FFFFFF;font-weight:600">{phase_pct}% ({phase_done}/{phase_total})</span>
            </div>
            <div class="progress-bar-bg">
                <div class="progress-bar-fill" style="width:{phase_pct}%"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # ── Next Up ───────────────────────────────────────────────────────────────
    next_tasks = [t for t in tasks if t["status"] in ("Next", "Done") == False and t["status"] == "Next"]
    high_pending = [t for t in tasks if t["status"] == "Pending" and t["priority"] == "High"][:3]

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<div class='section-card'><div class='section-card-title'>🔄 Sedang Dikerjakan</div>", unsafe_allow_html=True)
        if next_tasks:
            for t in next_tasks:
                st.markdown(f"""
                <div class="task-row">
                    <div>
                        <div class="task-name">{t['task']}</div>
                        <div class="task-meta">{t['tool']}</div>
                    </div>
                    <span class="phase-badge phase-next">Next</span>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown("<div style='font-size:13px;color:#6B6B8A;padding:8px 0'>Tidak ada task aktif</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='section-card'><div class='section-card-title'>🔥 High Priority — Pending</div>", unsafe_allow_html=True)
        if high_pending:
            for t in high_pending:
                st.markdown(f"""
                <div class="task-row">
                    <div>
                        <div class="task-name">{t['task']}</div>
                        <div class="task-meta">{t['tool']}</div>
                    </div>
                    <span class="phase-badge phase-pending">Pending</span>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown("<div style='font-size:13px;color:#6B6B8A;padding:8px 0'>Semua high priority selesai! 🎉</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
