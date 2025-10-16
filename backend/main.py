from fastapi import FastAPI
from routers import drivers, teams, results, history
from database import init_db

app = FastAPI(title="F1 API - FastAPI")

app.include_router(drivers.router)
app.include_router(teams.router)
app.include_router(results.router)
app.include_router(history.router)

@app.on_event("startup")
def startup():
    init_db()

@app.get("/")
def root():
    return {"message": "API F1 - Backend activo"}