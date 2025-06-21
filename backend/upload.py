from fastapi import  APIRouter,UploadFile, File,Depends,HTTPException
import requests
from backend.jwt_config import verify_token
import cloudinary
import cloudinary.uploader
from dotenv import load_dotenv
import os
load_dotenv()
cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET")
)

router = APIRouter()

@router.post("/upload")
async def upload_resume(file: UploadFile = File(...),payload: dict = Depends(verify_token) ):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    
    
    result = cloudinary.uploader.upload(
    file.file,
    upload_preset="ml_default",  
    resource_type="raw"           
    )  
    secure_url = result.get("secure_url")
    
     # Send to n8n webhook
    webhook_url = "https://leta.app.n8n.cloud/webhook-test/resume-analysis" #don't forget to store this in .env file
    try:
        n8n_response = requests.post(webhook_url, json={"pdf_url": secure_url})
        n8n_response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Failed to call n8n webhook: {e}")



    # You can save or parse PDF content here
    return {"filename": file.filename, "url":secure_url}
