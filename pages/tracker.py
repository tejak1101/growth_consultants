import streamlit as st
from pages.data_store import load_tasks, save_tasks, add_task, update_task, delete_task

STATUS_BADGE = {
    "Done":    "phase-done",
    "Next":    "phase-next",
    "Pending": "phase-pending",
}
STATUS_EMOJI = {"Done": "✅", "Next": "🔄", "Pending": "⏳"}
PRIORITY_COLOR = {"High": "#F87171", "Medium": "#FCD34D", "Low": "#6B6B8A"}

PHASES = ["Phase 1 — Foundation", "Phase 2 — Client System", "Phase 3 — Scale"]

def render():
    st.markdown("""
    <div class="page-header">
        <div class="page-eyebrow">ROADMAP</div>
        <div class="page-title">Project Tracker</div>
        <div class="page-sub">Tracking semua task setup & build Growth Consultants</div>
    </div>
    """, unsafe_allow_html=True)

    tasks = load_tasks()

    # ── Filter bar ──────────────────────────────────────────────────────────
    col1, col2, col3 = st.columns([2, 2, 2])
    with col1:
        filter_phase = st.selectbox("Phase", ["All"] + PHASES, key="filter_phase")
    with col2:
        filter_status = st.selectbox("Status", ["All", "Done", "Next", "Pending"], key="filter_status")
    with col3:
        filter_priority = st.selectbox("Priority", ["All", "High", "Medium", "Low"], key="filter_priority")

    filtered = tasks
    if filter_phase    != "All": filtered = [t for t in filtered if t["phase"]    == filter_phase]
    if filter_status   != "All": filtered = [t for t in filtered if t["status"]   == filter_status]
    if filter_priority != "All": filtered = [t for t in filtered if t["priority"] == filter_priority]

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Task list grouped by phase ───────────────────────────────────────────
    phases_to_show = PHASES if filter_phase == "All" else [filter_phase]

    for phase in phases_to_show:
        phase_tasks = [t for t in filtered if t["phase"] == phase]
        if not phase_tasks:
            continue

        done_count = sum(1 for t in phase_tasks if t["status"] == "Done")
        st.markdown(f"""
        <div class="section-card">
            <div class="section-card-title">
                {phase}
                <span style="font-size:12px;font-weight:400;color:#6B6B8A;margin-left:auto">
                    {done_count}/{len(phase_tasks)} selesai
                </span>
            </div>
        """, unsafe_allow_html=True)

        for t in phase_tasks:
            badge = STATUS_BADGE.get(t["status"], "phase-pending")
            pcolor = PRIORITY_COLOR.get(t["priority"], "#6B6B8A")

            col_a, col_b = st.columns([6, 1])
            with col_a:
                st.markdown(f"""
                <div class="task-row">
                    <div style="flex:1">
                        <div style="display:flex;align-items:center;gap:10px;margin-bottom:4px">
                            <div class="task-name">{t['task']}</div>
                            <span class="phase-badge {badge}">{STATUS_EMOJI[t['status']]} {t['status']}</span>
                            <span style="font-size:11px;font-weight:600;color:{pcolor}">● {t['priority']}</span>
                        </div>
                        <div class="task-meta">🔧 {t['tool']}
                            {"  ·  📝 " + t['notes'] if t.get('notes') else ""}
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            with col_b:
                if st.button("Edit", key=f"edit_{t['id']}"):
                    st.session_state[f"editing_{t['id']}"] = True

            # Inline edit form
            if st.session_state.get(f"editing_{t['id']}"):
                with st.form(key=f"form_{t['id']}"):
                    st.markdown(f"**Edit: {t['task']}**")
                    new_status   = st.selectbox("Status",   ["Done","Next","Pending"], index=["Done","Next","Pending"].index(t["status"]))
                    new_priority = st.selectbox("Priority", ["High","Medium","Low"],   index=["High","Medium","Low"].index(t["priority"]))
                    new_tool     = st.text_input("Tool", value=t["tool"])
                    new_notes    = st.text_area("Notes", value=t.get("notes",""), height=80)
                    c1, c2, c3 = st.columns(3)
                    with c1:
                        save_btn = st.form_submit_button("💾 Simpan")
                    with c2:
                        del_btn  = st.form_submit_button("🗑️ Hapus", type="secondary")
                    with c3:
                        cancel   = st.form_submit_button("✕ Cancel")

                    if save_btn:
                        update_task(t["id"], {"status": new_status, "priority": new_priority, "tool": new_tool, "notes": new_notes})
                        st.session_state[f"editing_{t['id']}"] = False
                        st.rerun()
                    if del_btn:
                        delete_task(t["id"])
                        st.session_state[f"editing_{t['id']}"] = False
                        st.rerun()
                    if cancel:
                        st.session_state[f"editing_{t['id']}"] = False
                        st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

    # ── Add New Task ─────────────────────────────────────────────────────────
    st.markdown("<br>", unsafe_allow_html=True)
    with st.expander("➕  Tambah Task Baru"):
        with st.form("add_task_form"):
            st.markdown("**Task Baru**")
            col1, col2 = st.columns(2)
            with col1:
                new_name     = st.text_input("Nama Task *")
                new_tool_add = st.text_input("Tool / Platform")
                new_phase    = st.selectbox("Phase", PHASES)
            with col2:
                new_stat     = st.selectbox("Status",   ["Pending","Next","Done"])
                new_prio     = st.selectbox("Priority", ["High","Medium","Low"])
                new_notes_add = st.text_area("Notes", height=80)

            submitted = st.form_submit_button("➕ Tambah Task", use_container_width=True)
            if submitted:
                if new_name.strip():
                    add_task({
                        "phase": new_phase, "task": new_name.strip(),
                        "tool": new_tool_add, "status": new_stat,
                        "priority": new_prio, "notes": new_notes_add,
                    })
                    st.success(f"Task '{new_name}' berhasil ditambahkan!")
                    st.rerun()
                else:
                    st.error("Nama task tidak boleh kosong.")
