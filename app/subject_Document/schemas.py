from pydantic import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer
from app.subject.schemas import Subject


class SubjectDocument(BaseModel):
    id: int
    subject_id: int
    user_id: int
    filefield: str


class SubjectDocumentDataId(BaseModel):
    subject_id: int
    user_id: int
    filefield: str


class SubjectDocumentCreate(BaseModel):
    subject_id: int
    user_id: int
    filefield: str


class SubjectDocumentGet(BaseModel):
    sub_doc_subject: Subject
    filefield: str

    class Config:
        orm_mode = True


class SubjectDataId(BaseModel):
    id: int
    sub_doc_subject: Subject

    class Config:
        orm_mode = True


class SubjectDocumentUpdate(BaseModel):
    filefield: str


