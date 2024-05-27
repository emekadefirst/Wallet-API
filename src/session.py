from .db import engine
from sqlmodel import Session, select
from .models import User, Account, AccountNumber, Wallet


class UserSession:
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
    
    def get_all(self):
        with Session(engine) as session:
            data = select(User)
            response = session.exec(data)
            return response
        
        
    def get_by_id(self):
        with Session(engine) as session:
            user = session.get(User, user.id)
            return user
        



