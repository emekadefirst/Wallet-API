from user import User
from wallet import Wallet
from typing import Optional
from src.db import create_db_and_tables
from sqlmodel import Field, SQLModel, Relationship



class Account(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(default=None, foreign_key="user.id", unique=True)
    firstname: Optional[str] = Field(max_length=20)
    lastname: Optional[str] = Field(max_length=20)
    othername: Optional[str] = Field(max_length=20)
    phonenumber: int
    bvn: int
    nin: int
    address: Optional[str] = Field(max_length=300)
    profile_image: str
    user: Optional[User] = Relationship(back_populates="account")
    account_number: Optional["AccountNumber"] = Relationship(back_populates="account")
    wallet: Optional["Wallet"] = Relationship(back_populates="account")

class AccountNumber(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    number: int
    account_id: int = Field(default=None, foreign_key="account.id", unique=True)
    account: Optional[Account] = Relationship(back_populates="account_number")
    

if __name__ == "__main__":
    create_db_and_tables()