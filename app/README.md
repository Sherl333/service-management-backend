# Service Membership API (FastAPI + PostgreSQL)

A simple membership management backend built using FastAPI, SQLModel, and PostgreSQL.  
Includes CRUD operations, search, filtering, tests, task scripts, and database migrations.

---

## Features

### Members API
- Create a member  
- List all members  
- Search (by name or phone)  
- Filter (by active/inactive status)

### Tests
- Pytest for search  and filter

### Database
- SQLModel models  
- Alembic migrations  
- Optional DB triggers  

### 🔧 Dev Tools
- `create_tables.py`
- `requirements.txt`
- `.env.example`

---

## 📦 Project Structure

```
service-membership/
├─ app/
│  ├─ __init__.py
│  ├─ main.py
│  ├─ database.py
│  ├─ models.py
│  ├─ schemas.py
│  ├─ crud.py
│  └─ routers/
│     ├─ __init__.py
│     ├─ members.py
│     ├─ plans.py
│     ├─ subscriptions.py
│     └─ attendance.py
├─ scripts/
│  └─ create_db.py       
├─ triggers.sql
├─ tests/
│  └─ test_members.py 
└─ README.md

```

---

## Installation

### Clone:
```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
```

---

## 🔐 Environment Variables

Create your `.env`:
```bash
cp .env.example .env
```

Update:
```
DATABASE_URL=postgresql://postgres:MyPassword@localhost:5432/service_membership
```

⚠️ Do NOT upload `.env` to GitHub.

---

## 📥 Install Dependencies

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 🛢 Create Database Tables

### Option 1 — Use script:
```bash
python create_tables.py
```

### Option 2 — Alembic:
```bash
alembic upgrade head
```

---

## ▶️ Run FastAPI

```bash
uvicorn app.main:app --reload
```

Docs:
```
http://127.0.0.1:8000/docs
```

---

## 🔎 Search & Filter

### Search:
```
GET /members/search?q=john
```

### Filter:
```
GET /members/filter?status=active
```

---

## 🧪 Run Tests

```bash
pytest
```

---

## 🧰 Database Triggers (Optional)

Run:
```bash
psql -d service_membership -f triggers.sql
```

---

## 🛠 Deploying Without Exposing DB Password

1. Commit `.env.example` (safe)
2. Do NOT commit `.env`
3. On Render / Railway:
   - Add environment variable:  
     ```
     DATABASE_URL=
     ```
4. Deploy — your password stays private.

---

## 📄 License
MIT

---

## 👩‍💻 Author  
Sherlin Manuel  
