# Restaverse Assignment

**Employee Directory Search** — React + Vite · FastAPI · MySQL

> Type **"Rah"**. Most search bars send 3 requests.
> This one sends **1** — and cancels it if you keep typing.

Curious how? The answer is spread across `frontend/` and `backend/`. Start with the search hook, then follow the request all the way down to the index it hits in MySQL.

---

### Quick start

```bash
# backend
cd backend && pip install -r requirements.txt && cp .env.example .env
uvicorn app.main:app --reload

# frontend
cd frontend/employee_management && npm install && cp .env.example .env
npm run dev
```

---

_Built by **Joe Nadar**. Every decision in here has a reason — ask me about any of them._
