from typing import Optional
from src.db import create_db_and_tables
from sqlmodel import Field, SQLModel, Relationship
from account import Account

class Wallet(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    account: Optional[Account] = Relationship(back_populates="wallet")
    balance: float = Field(default=0.00)



if __name__ == "__main__":
    create_db_and_tables()