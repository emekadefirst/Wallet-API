from fastapi import FastAPI
from sqlmodel import SQLModel, create_engine

app = FastAPI()
file_name = "server.db"
sqlite_url = f'sqlite:///{file_name}'
engine = create_engine(sqlite_url, echo=True)
SQLModel.metadata.create_all(engine)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
