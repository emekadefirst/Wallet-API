from main import engine
from model import Account
from sqlmodel import Session, select


class AccountSession:
    def __init__(self, user_id: int, firstname: str, lastname: str, othername: str, 
                 phonenumber: int, bvn: int, nin: int, address: str, profile_image=None):
        self.user_id = user_id
        self.firstname = firstname
        self.lastname = lastname
        self.othername = othername
        self.phonenumber = phonenumber
        self.bvn = bvn
        self.nin = nin
        self.address = address
        self.profile_image = profile_image
        
    def create(self):
        try:
            with Session(engine) as session:
                account = Account(
                    user_id=self.user_id,
                    firstname=self.firstname,
                    lastname=self.lastname,
                    othername=self.othername,
                    phonenumber=self.phonenumber,
                    bvn=self.bvn,
                    nin=self.nin,
                    address=self.address,
                    profile_image=self.profile_image
                )
                session.add(account)
                session.commit()
                session.refresh(account)
                return f"User added with ID: {account.id}"
        except Exception as e:
            return f"Error in adding user: {e}"
    @staticmethod   
    def get_all():
        with Session(engine) as session:
            statement = select(Account)
            response = session.exec(statement)
            return response.all()
    @staticmethod
    def get_by_id(account_id: int):
        with Session(engine) as session:
            account = session.get(Account, account_id)
            return account
        

    def update(self, account_id: int):
        try:
            with Session(engine) as session:
                account = session.get(Account, self.account_id)
                if account:
                    account.user_id = self.user_id
                    account.firstname = self.firstname
                    account.lastname = self.lastname
                    account.othername = self.othername
                    account.phonenumber = self.phonenumber
                    account.bvn = self.bvn
                    account.nin = self.nin
                    account.address = self.address
                    account.profile_image = self.profile_image
                    session.commit()
                    session.refresh(account)
                    return f"Account updated with ID: {account.id}"
                else:
                    return f"Account with ID: {self.account_id} not found"
        except Exception as e:
            return f"Error in updating account: {e}"