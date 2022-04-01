from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from app.sem import schemas
from app.sem.schemas import SemesterBranchID,SemesterBody
from database import get_db
from app.sem.models import Semester
from app.branch.models import Branch
from typing import List
from app.users.oauth import get_current_url
from app.users.schemas import UserCreate

router = APIRouter(
    prefix="/semester",
    tags=['semseter']
)

@router.post('/', response_model=SemesterBranchID)
def create(request: SemesterBody,db: Session = Depends(get_db),get_current_user:UserCreate = Depends(get_current_url)):
    data = db.query(Branch).get(request.branch_id)
    print(data.name)
    sem_data_create = Semester(name = request.name, branch_id=data.id)
    db.add(sem_data_create)
    db.commit()
    db.refresh(sem_data_create)
    return sem_data_create.__dict__


@router.get('/', response_model=List[schemas.SemsterwithId])
def show_record(db: Session = Depends(get_db),get_current_user:UserCreate = Depends(get_current_url)):
    semester = db.query(Semester).all()
    return semester


@router.get('/{id}', response_model=SemesterBranchID)
def get_record(id, db: Session = Depends(get_db),get_current_user:UserCreate = Depends(get_current_url)):
    get_data = db.query(Semester).filter(Semester.id == id).first()
    if not get_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Semester with the id {id} not found")
    return get_data

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update_sem_record(id, request: schemas.SemesterUpdate, db: Session = Depends(get_db),get_current_user:UserCreate = Depends(get_current_url)):
    update_sem = db.query(Semester).filter(Semester.id==id)
    if not update_sem:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Semester with the id {id} not found")
    update_sem.update(request.dict())
    db.commit()
    return "Record Updated in Database"


@router.delete('/{id}')
def destroy(id, db: Session = Depends(get_db),get_current_user:UserCreate = Depends(get_current_url)):
    delete_sem_record = db.query(Semester).filter(Semester.id == id)
    if not delete_sem_record.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Semester with the id {id} not found")
    delete_sem_record.delete(synchronize_session=False)
    db.commit()
    return "Record Deleted from Database"

