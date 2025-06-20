from fastapi import  APIRouter,UploadFile, File,Depends
from backend.jwt_config import verify_token

router = APIRouter()

@router.post("/upload")
async def upload_resume(file: UploadFile = File(...),payload: dict = Depends(verify_token) ):
    content = await file.read()
    # You can save or parse PDF content here
    return {"filename": file.filename, "size": len(content),}
