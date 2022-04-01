from fastapi import FastAPI, APIRouter, Depends, HTTPException, status
from app.users.models import User
from app.users import schemas
from sqlalchemy.orm import Session
from database import get_db
from hashing import Hash
from datetime import datetime, timedelta
from app.users.token import create_access_token
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/login",
    tags=["authentications_login"]
)


SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


@router.post('/')
def login(request:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials")

    if not Hash.verify(user.hashed_password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Password")
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

