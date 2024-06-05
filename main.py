import uvicorn
from fastapi import FastAPI
from database import create_db_and_tables
from app import auth

app = FastAPI()

app.include_router(auth)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
