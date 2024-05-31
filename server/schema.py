from pydantic import BaseModel

class Wallet(BaseModel):
    pass

class User(BaseModel):
    username : str
    email : str
    password : str

class Account(BaseModel):
    user_id : int
    firstname : str 
    lastname : str
    othername : str
    phonenumber : int
    bvn : int
    nin : int
    address : str
    profile_image : str