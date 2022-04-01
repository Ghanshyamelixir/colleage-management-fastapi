from sqlalchemy.orm import Session
from database import get_db
from fastapi import APIRouter, Depends
from app.users.models import User
from app.users import schemas
from hashing import Hash

route = APIRouter(
    prefix="/user",
    tags=["user"]
)

@route.post('/', response_model=schemas.UserResponse)
def CreateUser(request: schemas.UserCreate, db: Session = Depends(get_db)):
    user_create = User(email = request.email, hashed_password = Hash.bcrypt(request.hashed_password))
    db.add(user_create)
    db.commit()
    db.refresh(user_create)
    return user_create.__dict__

