# Taskflow — Task Manager Web App

A full-stack task manager built with **FastAPI**, **SQLite**, and vanilla **HTML/CSS/JS**.

## Features

- Add, edit, complete, and delete tasks
- Optional task descriptions
- Filter by All / Pending / Done
- Input validation (empty titles rejected, length limits enforced)
- Persistent storage via SQLite
- Clean dark UI with toast notifications

## Tech Stack

| Layer    | Technology            |
|----------|-----------------------|
| Backend  | FastAPI + SQLAlchemy  |
| Database | SQLite                |
| Frontend | HTML / CSS / JS       |
| Deploy   | Railway               |

## Local Setup

**Requirements:** Python 3.9+

```bash
git clone https://github.com/<your-username>/task-manager.git
cd task-manager

python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements.txt

uvicorn main:app --reload
```

Open [http://localhost:8000](http://localhost:8000).

## API Endpoints

| Method | Endpoint     | Description    |
|--------|--------------|----------------|
| GET    | /tasks       | List all tasks |
| POST   | /tasks       | Create a task  |
| PUT    | /tasks/{id}  | Update a task  |
| DELETE | /tasks/{id}  | Delete a task  |

Interactive API docs are available at `/docs`.

## Deploy to Railway

1. Push this repo to GitHub.
2. Go to [railway.app](https://railway.app) → **New Project** → **Deploy from GitHub repo**.
3. Select your repository — Railway auto-detects Python and installs dependencies.
4. Go to **Settings → Networking → Generate Domain** to get your public URL.

## Project Structure

```
task-manager/
├── main.py          # FastAPI app and route handlers
├── models.py        # SQLAlchemy Task model
├── schemas.py       # Pydantic request/response schemas
├── database.py      # DB engine and session setup
├── static/
│   └── index.html   # Single-page frontend
├── requirements.txt
├── railway.toml     # Railway deployment config
└── README.md
```
