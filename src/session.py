import enum
from sqlmodel import Session
from .db import engine
from .models import User, Account, AccountNumber, Wallet


class User:
    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.password = password

    def add(self) -> str:
        try:
            with Session(engine) as session:
                user = User(username=self.username, email=self.email, password=self.password)
                session.add(user)
                session.commit()
                session.refresh(user)
                return f"User added with ID: {user.id}"
        except Exception as e:
            return f"Error in adding user: {e}"



