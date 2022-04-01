from pydantic import BaseModel
from typing import List
from app.sem.schemas import Semester


class Subject(BaseModel):
    id: int
    name: str
    semester_id: int

    class Config:
        orm_mode = True


class SubjectSemId(BaseModel):
    name: str
    semester_id: int

    class Config:
        orm_mode = True


class SubjectDataList(BaseModel):
    name: str
    semester_id: int
    subject_semesters: Semester

    class Config:
        orm_mode = True


class SubjectUpdate(BaseModel):
    name: str

    class Config:
        orm_mode = True