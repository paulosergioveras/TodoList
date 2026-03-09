# To-Do List Django Fullstack

A simple To-Do list application built with **Django** using server-rendered templates.

---

## 🚀 Quick Start (Local)

### 1) Clone / open this repository

```bash
git clone <repo-url>
cd to-do-list-django-fullstack
```

### 2) Create a Python virtual environment

```bash
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Configure environment variables

Copy the example environment file:

```bash
copy .env.example .env
```

> The default `.env.example` is ready for local development. No changes are required unless you want to customize settings.

### 5) Apply database migrations

```bash
python manage.py migrate
```

### 6) Create superuser

```bash
python manage.py createsuperuser
```

### 7) Run the development server

```bash
python manage.py runserver
```

Open in your browser:

- http://localhost:8000/
- Admin panel: http://localhost:8000/admin/

---

## 🐳 Run with Docker

```bash
docker-compose up --build
```

Then open:

- http://localhost:8000/

---

## 📝 Notes

- The default local database is SQLite (`db.sqlite3`).
- Set `DJANGO_ENV=prd` in `.env` to use PostgreSQL (configured via `POSTGRES_*` env vars).

---

## 📄 License

This project is released under the MIT License.
