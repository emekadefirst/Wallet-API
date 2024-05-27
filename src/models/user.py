from typing import Optional
from src.db import create_db_and_tables
from sqlmodel import Field, SQLModel, Relationship
from account import Account

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(default=None, unique=True, max_length=15)
    email: str = Field(default=None, unique=True, max_length=30)
    password: str
    account: Optional["Account"] = Relationship(back_populates="user")
    
    
if __name__ == "__main__":
    create_db_and_tables()