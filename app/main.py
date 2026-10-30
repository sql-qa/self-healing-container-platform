import os

import psycopg
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

DATABASE_URL = os.environ.get(
    "DATABASE_URL", "postgresql://notes:notes@localhost:5432/notes"
)

app = FastAPI(title="Notes API")


class Note(BaseModel):
    text: str


def get_conn():
    return psycopg.connect(DATABASE_URL, connect_timeout=3)


def ensure_table(conn):
    conn.execute(
        "CREATE TABLE IF NOT EXISTS notes (id SERIAL PRIMARY KEY, text TEXT NOT NULL)"
    )


@app.get("/health")
def health():
    # lets see if the app runs how it supposed to
    return {"status": "ok"}


@app.get("/ready")
def ready():
    # here i want to see if the app connects to the db
    try:
        with get_conn() as conn:
            conn.execute("SELECT 1")
        return {"status": "ready"}
    except psycopg.OperationalError:
        raise HTTPException(status_code=503, detail="database unavailable")


@app.get("/notes")
def list_notes():
    try:
        with get_conn() as conn:
            ensure_table(conn)
            rows = conn.execute("SELECT id, text FROM notes ORDER BY id").fetchall()
        return [{"id": r[0], "text": r[1]} for r in rows]
    except psycopg.OperationalError:
        raise HTTPException(status_code=503, detail="database unavailable")


@app.post("/notes", status_code=201)
def add_note(note: Note):
    try:
        with get_conn() as conn:
            ensure_table(conn)
            row = conn.execute(
                "INSERT INTO notes (text) VALUES (%s) RETURNING id", (note.text,)
            ).fetchone()
        return {"id": row[0], "text": note.text}
    except psycopg.OperationalError:
        raise HTTPException(status_code=503, detail="database unavailable")
