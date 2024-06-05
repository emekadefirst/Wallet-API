from sqlmodel import SQLModel, create_engine
from account.model import Account
from wallet.model import Wallet
from user.model import User

file_name = "server.db"
sqlite_url = f'sqlite:///{file_name}'
engine = create_engine(sqlite_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
