from fastapi import APIRouter, File, UploadFile, HTTPException
import os

router = APIRouter()

# Allowed file types and extensions
ALLOWED_EXTENSIONS = [
    "application/vnd.ms-powerpoint",  # .ppt
    "application/vnd.openxmlformats-officedocument.presentationml.presentation",  # .pptx
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",  # .docx
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",  # .xlsx
]

@router.post("/upload-file/")
async def upload_file(file: UploadFile = File(...)):
    if not file:
        raise HTTPException(status_code=400, detail="No file uploaded")

    # Check file content type against allowed types
    if file.content_type not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail="Invalid file type")

    # Optionally, check file extension for additional verification
    filename = file.filename.lower()
    if not any(filename.endswith(ext) for ext in [".pptx", ".docx", ".xlsx"]):
        raise HTTPException(status_code=400, detail="Invalid file extension")

    # Read file content
    file_content = await file.read()

    return {"filename": file.filename, "content_size": len(file_content)}

