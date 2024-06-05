from pydantic import BaseModel

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