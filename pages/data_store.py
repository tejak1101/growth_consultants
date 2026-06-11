import json
from pathlib import Path
from datetime import datetime

DATA_DIR = Path(__file__).parent.parent / "data"
DATA_DIR.mkdir(exist_ok=True)

# ── File paths ──────────────────────────────────────────────────────────────
TASKS_FILE     = DATA_DIR / "tasks.json"
CLIENTS_FILE   = DATA_DIR / "clients.json"
CHECKLIST_FILE = DATA_DIR / "checklist.json"

# ── Default data ─────────────────────────────────────────────────────────────
DEFAULT_TASKS = [
    # Phase 1
    {"id": 1, "phase": "Phase 1 — Foundation", "task": "Discord Server Setup",           "tool": "Discord",            "status": "Done",    "priority": "High",   "notes": "Server Growth Consultants sudah dibuat"},
    {"id": 2, "phase": "Phase 1 — Foundation", "task": "Channel Structure Created",       "tool": "Discord",            "status": "Done",    "priority": "High",   "notes": "Semua kategori dan channel dengan emoji"},
    {"id": 3, "phase": "Phase 1 — Foundation", "task": "Admin Access Granted",            "tool": "Discord",            "status": "Done",    "priority": "High",   "notes": "Teja sudah di-admin-in oleh bos"},
    {"id": 4, "phase": "Phase 1 — Foundation", "task": "Zapier — Discord Automations",   "tool": "Zapier + Discord",   "status": "Next",    "priority": "High",   "notes": "Connect Typeform, GHL, Stripe ke Discord"},
    {"id": 5, "phase": "Phase 1 — Foundation", "task": "Email Service Provider (Kit)",   "tool": "Kit / ConvertKit",   "status": "Pending", "priority": "Medium", "notes": "Buat akun di kit.com"},
    {"id": 6, "phase": "Phase 1 — Foundation", "task": "CRM Setup — GoHighLevel",        "tool": "GoHighLevel",        "status": "Pending", "priority": "High",   "notes": "Setup dashboard, calendar, pipeline"},
    {"id": 7, "phase": "Phase 1 — Foundation", "task": "Typeform Application Setup",     "tool": "Typeform",           "status": "Pending", "priority": "High",   "notes": "DQ logic: <3K dan 3-5K"},
    {"id": 8, "phase": "Phase 1 — Foundation", "task": "Payment Processor (Stripe)",     "tool": "Stripe / Whop",      "status": "Pending", "priority": "Medium", "notes": "Connect ke Zapier untuk notif"},
    # Phase 2
    {"id": 9,  "phase": "Phase 2 — Client System", "task": "Client Onboarding Process",  "tool": "GHL + Discord",      "status": "Pending", "priority": "High",   "notes": "Buat flow onboarding terstruktur"},
    {"id": 10, "phase": "Phase 2 — Client System", "task": "Setter Tracking Sheet",      "tool": "Google Sheets",      "status": "Pending", "priority": "Medium", "notes": "UTM links + tracking harian"},
    {"id": 11, "phase": "Phase 2 — Client System", "task": "Closing Script from Offer",  "tool": "Docs",               "status": "Pending", "priority": "High",   "notes": "2-step closing script template"},
    {"id": 12, "phase": "Phase 2 — Client System", "task": "Closer Tracking Sheet",      "tool": "Google Sheets",      "status": "Pending", "priority": "Medium", "notes": "Sales tracker harian"},
    {"id": 13, "phase": "Phase 2 — Client System", "task": "Daily Team Call Schedule",   "tool": "Discord + Zoom",     "status": "Pending", "priority": "Medium", "notes": "Morning check-in + evening EOD"},
    {"id": 14, "phase": "Phase 2 — Client System", "task": "Freebie / Lead Magnet",      "tool": "Canva + Kit",        "status": "Pending", "priority": "Low",    "notes": "Connect ke email opt-in funnel"},
    # Phase 3
    {"id": 15, "phase": "Phase 3 — Scale",        "task": "Facebook Ads Setup",          "tool": "Meta Ads Manager",   "status": "Pending", "priority": "High",   "notes": "Untuk bisnis sendiri (bukan klien)"},
    {"id": 16, "phase": "Phase 3 — Scale",        "task": "Low-Ticket Funnel",           "tool": "GHL + Whop",         "status": "Pending", "priority": "Low",    "notes": "#low-ticket-lead channel"},
    {"id": 17, "phase": "Phase 3 — Scale",        "task": "ManyChat IG Automation",      "tool": "ManyChat",           "status": "Pending", "priority": "Medium", "notes": "IG/FB DM automation"},
    {"id": 18, "phase": "Phase 3 — Scale",        "task": "Weekly Promo Schedule",       "tool": "Kit + IG",           "status": "Pending", "priority": "Low",    "notes": "Email + IG stories promo"},
]

DEFAULT_CLIENTS = [
    {
        "id": 1,
        "name": "Dylan",
        "business": "VSL Funnel — Coaching",
        "status": "Active",
        "funnel_type": "VSL Funnel",
        "monthly_revenue": "5,000",
        "start_date": "2024-01-01",
        "notes": "VSL funnel aktif. Typeform DQ diupdate ke 3-5K. Telegram handler untuk DQ leads.",
        "platforms": "Facebook Ads, GoHighLevel, Typeform, Telegram",
    },
]

# ── CRUD helpers ─────────────────────────────────────────────────────────────
def load(file, default):
    if file.exists():
        with open(file) as f:
            return json.load(f)
    save(file, default)
    return default

def save(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# Tasks
def load_tasks():   return load(TASKS_FILE, DEFAULT_TASKS)
def save_tasks(d):  save(TASKS_FILE, d)

def add_task(task_dict):
    tasks = load_tasks()
    task_dict["id"] = max((t["id"] for t in tasks), default=0) + 1
    tasks.append(task_dict)
    save_tasks(tasks)

def update_task(task_id, updated):
    tasks = load_tasks()
    for i, t in enumerate(tasks):
        if t["id"] == task_id:
            tasks[i].update(updated)
    save_tasks(tasks)

def delete_task(task_id):
    tasks = [t for t in load_tasks() if t["id"] != task_id]
    save_tasks(tasks)

# Clients
def load_clients():   return load(CLIENTS_FILE, DEFAULT_CLIENTS)
def save_clients(d):  save(CLIENTS_FILE, d)

def add_client(client_dict):
    clients = load_clients()
    client_dict["id"] = max((c["id"] for c in clients), default=0) + 1
    clients.append(client_dict)
    save_clients(clients)

def update_client(client_id, updated):
    clients = load_clients()
    for i, c in enumerate(clients):
        if c["id"] == client_id:
            clients[i].update(updated)
    save_clients(clients)

def delete_client(client_id):
    clients = [c for c in load_clients() if c["id"] != client_id]
    save_clients(clients)

# Checklist
# Stored as: { "step_1_item_0": True, "step_2_item_3": False, ... }
def load_checklist():   return load(CHECKLIST_FILE, {})
def save_checklist(d):  save(CHECKLIST_FILE, d)

def get_check(step_num, item_idx, default=False):
    key = f"step_{step_num}_item_{item_idx}"
    return load_checklist().get(key, default)

def set_check(step_num, item_idx, value):
    data = load_checklist()
    data[f"step_{step_num}_item_{item_idx}"] = value
    save_checklist(data)
