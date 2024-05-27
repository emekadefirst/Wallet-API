from ..db import engine
from src.models.wallet import Wallet
from sqlmodel import Session, select


class WalletSession:
    def __init__(self, account_id: int, balance: float):
        self.account_id = account_id
        self.balance = balance

    def create(self) -> str:
        try:
            with Session(engine) as session:
                wallet = Wallet(
                    account_id=self.account_id,
                    balance=self.balance
                )
                session.add(wallet)
                session.commit()
                session.refresh(wallet)
                return f"Wallet created with ID: {wallet.id}"
        except Exception as e:
            return f"Error in creating wallet: {e}"
    
    @staticmethod   
    def get_all():
        with Session(engine) as session:
            statement = select(Wallet)
            response = session.exec(statement)
            return response.all()
        
    @staticmethod
    def get_by_id(wallet_id: int):
        with Session(engine) as session:
            wallet = session.get(Wallet, wallet_id)
            return wallet

    def update(self, wallet_id: int) -> str:
        try:
            with Session(engine) as session:
                wallet = session.get(Wallet, wallet_id)
                if wallet:
                    wallet.account_id = self.account_id
                    wallet.balance = self.balance
                    session.commit()
                    session.refresh(wallet)
                    return f"Wallet updated with ID: {wallet.id}"
                else:
                    return f"Wallet with ID: {wallet_id} not found"
        except Exception as e:
            return f"Error in updating wallet: {e}"