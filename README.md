# 🚀 Growth Consultants — Business OS

App Streamlit untuk manage project, clients, dan onboarding steps Growth Consultants.

## Struktur File

```
growth_consultants/
├── app.py                  # Entry point utama
├── requirements.txt        # Dependencies
├── assets/
│   └── style.css           # Styling dark theme
├── data/                   # Auto-generated saat pertama run
│   ├── tasks.json
│   └── clients.json
└── pages/
    ├── __init__.py
    ├── data_store.py       # CRUD helper (JSON storage)
    ├── dashboard.py        # Halaman dashboard & overview
    ├── tracker.py          # Project tracker dengan filter & edit
    ├── clients.py          # Client management (CRM lite)
    ├── onboarding.py       # Step-by-step onboarding guide
    └── tools.py            # Tools & tech stack overview
```

## Cara Menjalankan

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Jalankan app
```bash
streamlit run app.py
```

### 3. Buka browser
App akan otomatis terbuka di `http://localhost:8501`

## Fitur

| Halaman | Fitur |
|---------|-------|
| **Dashboard** | Overview metrics, funnel visual, phase progress, next tasks |
| **Project Tracker** | Filter by phase/status/priority, edit inline, tambah/hapus task |
| **Clients** | Tambah/edit/hapus klien, status tracking, detail per klien |
| **Onboarding Steps** | Panduan lengkap setup per step dengan checklist |
| **Tools & Stack** | Overview semua tools, connection diagram |

## Data Storage
Semua data disimpan di folder `data/` sebagai JSON file lokal.
Tidak perlu database atau internet connection.
