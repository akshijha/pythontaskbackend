from fastapi import APIRouter, UploadFile, HTTPException
from app.utils.file_utils import validate_and_save_file

router = APIRouter()

@router.post("/upload")
def upload_file(file: UploadFile):
    if not file.filename.endswith(('.pptx', '.docx', '.xlsx')):
        raise HTTPException(status_code=400, detail="Invalid file type")
    validate_and_save_file(file)
    return {"message": f"File '{file.filename}' uploaded successfully"}
