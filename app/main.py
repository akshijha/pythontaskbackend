from fastapi import FastAPI
from app.routers import ops_user, client_user
from app.routers.file_upload import router as file_upload_router

app = FastAPI()

# Include all routers
app.include_router(ops_user.router, prefix="/ops", tags=["Ops User"])
app.include_router(client_user.router, prefix="/client", tags=["Client User"])
app.include_router(file_upload_router, prefix="/file-upload", tags=["File Upload"])

@app.get("/")
def home():
    return {"message": "Welcome to the Secure File Sharing System"}
