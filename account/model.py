from user.model import User
from typing import Optional
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
    account_number: int
