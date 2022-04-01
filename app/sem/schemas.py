from pydantic import BaseModel
from typing import List
from app.branch.schemas import BranchName

class BranchSemester(BaseModel):
    name: str


class Semester(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class SemesterBranchID(BaseModel):
    name: str
    branch_id: int
    class Config():
        orm_mode = True


class SemesterBody(BaseModel):
    name: str
    branch_id : int
    class Config:
        orm_mode = True


class SemsterwithId(BaseModel):
    name: str
    branch_id: int
    sem_branch : BranchName

    class Config:
        orm_mode = True


class SemesterUpdate(BaseModel):
    name: str
    class Config:
        orm_mode = True

