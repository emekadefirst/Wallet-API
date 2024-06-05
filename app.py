from fastapi import APIRouter, HTTPException
from user.schema import UserSerializer
from user.session import UserSession

auth = APIRouter()

@auth.post('/user')
def create_user(user: UserSerializer):
    try:
        data = UserSession(user)
        data.add()
        return {"message": "User created successfully", "user": data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
