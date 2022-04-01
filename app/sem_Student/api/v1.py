from sqlalchemy.orm import Session
from database import get_db
from fastapi import Depends, APIRouter, HTTPException, status
from app.sem_Student.models import SemesterStudent
from app.sem_Student import schemas
from app.sem.models import Semester
from app.users.models import User
from app.sem_Student.schemas import SemesterSudentGetRecord
from typing import List
from app.users.oauth import get_current_url
from app.users.schemas import UserCreate


route = APIRouter(
    prefix="/semestersubject",
    tags=["semestersubject"]
)


@route.post('/', response_model=schemas.SemUserID)
def create_sem_sub(request: schemas.SemesterStudentData, db: Session = Depends(get_db),get_current_user:UserCreate = Depends(get_current_url)):
    semester_id = db.query(Semester).get(request.semester_id)
    user_id = db.query(User).get(request.user_id)
    semester_student_create_id = SemesterStudent(semester_id= semester_id.id, user_id=user_id.id)
    db.add(semester_student_create_id)
    db.commit()
    db.refresh(semester_student_create_id)
    return semester_student_create_id.__dict__


@route.get('/',response_model=List[SemesterSudentGetRecord])
def getdata(db: Session = Depends(get_db),get_current_user:UserCreate = Depends(get_current_url)):
    alldata = db.query(SemesterStudent).all()
    return alldata


@route.get('/{id}', response_model=schemas.SemesterStudentUsingId)
def getdata(id, db: Session = Depends(get_db),get_current_user:UserCreate = Depends(get_current_url)):
    getdata = db.query(SemesterStudent).filter(SemesterStudent.id == id).first()
    if not getdata:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"SemesterStudent with id {id} Not Found")
    return getdata

