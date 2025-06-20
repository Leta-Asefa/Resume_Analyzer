from fastapi import APIRouter,Body,HTTPException
from backend.jwt_config import create_access_token
router=APIRouter()

@router.get('/login')
async def login(username:str=Body(...) ,password:str=Body(...)):
    if not username or not password:
        raise HTTPException(
            status_code=400,
            detail="Username and password cannot be empty"
        )
    if username != 'test' or password != '1234':
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )
    
    token=create_access_token(data={'sub':username,})
    
    return {"message": "Logged in successfully", "username": username,"token":token}