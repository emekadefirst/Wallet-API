from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from account.model import Account

class Wallet(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    account: Optional[Account] = Relationship(back_populates="wallet")
    balance: float = Field(default=0.00)


