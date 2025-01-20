import os

UPLOAD_FOLDER = "uploaded_files"

def validate_and_save_file(file):
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    with open(os.path.join(UPLOAD_FOLDER, file.filename), "wb") as f:
        f.write(file.file.read())
