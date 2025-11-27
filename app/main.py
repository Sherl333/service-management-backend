# app/main.py
from fastapi import FastAPI
from app.database import create_db_and_tables
from app.routers import members, plans, subscriptions, attendance

app = FastAPI(title="Service Membership API")

# create tables if running locally - in production you may replace with migrations
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/users/search")
def search_users(q: str):
    statement = select(User).where(User.name.ilike(f"%{q}%"))
    results = session.exec(statement).all()
    return results
@app.get("/users/filter")
def filter_users(role: str | None = None):
    statement = select(User)
    if role:
        statement = statement.where(User.role == role)
    return session.exec(statement).all()


app.include_router(members.router)
app.include_router(plans.router)
app.include_router(subscriptions.router)
app.include_router(attendance.router)
