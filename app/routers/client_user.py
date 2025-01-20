from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_client_user():
    return {"message": "Client user endpoint working!"}
