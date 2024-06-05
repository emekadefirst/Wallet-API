from typing import Optional
from sqlmodel import Field, SQLModel, Relationship


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(default=None, unique=True, max_length=15)
    email: str = Field(default=None, unique=True, max_length=30)
    password: str

    
    
