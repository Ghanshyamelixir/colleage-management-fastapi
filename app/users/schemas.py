from pydantic import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
# from app.sem_Student.schemas import SemesterStudent
# from app.subject_Document.schemas import SubjectDocument


class User(BaseModel):
    id : int
    email : str
    hashed_password : str
    # user_sem_subject = SemesterStudent
    # user_sub_doc = SubjectDocument

    class Config:
        orm_mode = True


class UserResponse(BaseModel):
    email : str
    hashed_password : str


class UserCreate(BaseModel):
    email: str
    hashed_password : str


class Token(BaseModel):
    access_token: str
    token_type: str
