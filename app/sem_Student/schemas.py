from pydantic import BaseModel
from app.sem.schemas import Semester

class SemesterStudent(BaseModel):
    id: int
    semester_id: int
    user_id: int

    class Config:
        orm_mode = True


class SemUserID(BaseModel):
    semester_id: int
    user_id: int


class SemesterStudentData(BaseModel):
    semester_id: int
    user_id: int


class SemesterSudentGetRecord(BaseModel):
    sem_stu_semester: Semester

    class Config:
        orm_mode = True


class SemesterStudentUsingId(BaseModel):
    id: int
    sem_stu_semester: Semester

    class Config:
        orm_mode = True
