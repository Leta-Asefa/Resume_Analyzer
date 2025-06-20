from fastapi import APIRouter,Body,HTTPException
from backend.jwt_config import create_access_token
from pydantic import BaseModel,Field
router=APIRouter()

class LoginRequest(BaseModel):
    username: str = Field(..., min_length=3, max_length=20)
    password: str = Field(..., min_length=8)



@router.post('/login')
async def login(data:LoginRequest):
    if data.username != 'test' or data.password != '12345678': #will  be checked from database 
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )
    
    token=create_access_token(data={'sub':data.username,})
    
    return {"message": "Logged in successfully", "username": data.username,"token":token}