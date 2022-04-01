from sqlalchemy.orm import Session
from database import get_db
from app.sem.schemas import *
from app.sem.models import Semester
from app.subject.models import Subject
from app.subject import schemas
from fastapi import APIRouter, Depends, HTTPException, status
from app.subject.schemas import SubjectDataList

router = APIRouter(
    prefix="/subject",
    tags=["subject"]
)


@router.post('/', response_model=schemas.SubjectSemId)
def create_subject_data(request: schemas.Subject, db: Session = Depends(get_db)):
    semester_id = db.query(Semester).get(request.semester_id)
    semester_data_create = Subject(name=request.name, semester_id=semester_id.id)
    db.add(semester_data_create)
    db.commit()
    db.refresh(semester_data_create)
    return semester_data_create.__dict__


@router.get('/', response_model=List[SubjectDataList])
def get_subject_record(db: Session = Depends(get_db)):
    alldata = db.query(Subject).all()
    return alldata


@router.get('/{id}', response_model=schemas.SubjectSemId)
def get_record(id, db: Session = Depends(get_db)):
    getdata = db.query(Subject).filter(Subject.id == id).first()
    if not getdata:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Subject with the id {id} not found")
    return getdata


@router.put('/{id}')
def update_record(id, request: schemas.SubjectUpdate, db: Session = Depends(get_db)):
    update_data = db.query(Subject).filter(Subject.id == id)
    if not update_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Semester with the id {id} not found")
    update_data.update(request.dict())
    db.commit()
    return "Record Updated in Database"


