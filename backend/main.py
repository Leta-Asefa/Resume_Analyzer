# main.py
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from backend.upload import router as upload_router  # Import the router
from backend.auth import router as auth_router  # Import the router

app = FastAPI()

# Allow requests from your frontend (if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload_router)
app.include_router(auth_router)


@app.get("/") # Default Root Endpoint
async def root():
    return {"message": "Resume Analyzer API"}