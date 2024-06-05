from pydantic import BaseModel

class Wallet(BaseModel):
    pass

class User(BaseModel):
    username : str
    email : str
    password : str

