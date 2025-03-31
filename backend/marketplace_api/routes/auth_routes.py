from fastapi import APIRouter, Depends
from ..schemas.user_schema import UserCreate, UserRead

router = APIRouter()

@router.post("/signup", response_model=UserRead)
def signup(user_data: UserCreate):
    # Implement user creation logic
    return {"id": 1, "email": user_data.email, "full_name": user_data.full_name}
