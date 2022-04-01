from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from app.branch import schemas
from app.branch.models import Branch
from database import get_db
from typing import List

router = APIRouter(
    prefix="/branch",
    tags=['branch']
)


@router.post('/', response_model=schemas.BranchNameResponse)
def branch_create(request: schemas.BranchName, db: Session = Depends(get_db)):
    branch_data = Branch(name=request.name)

    db.add(branch_data)
    db.commit()
    db.refresh(branch_data)
    # print(branch_data.__dict__)
    return branch_data.__dict__


@router.get('/', response_model=List[schemas.BranchName])
def list_of_data(db: Session = Depends(get_db)):
    showdata = db.query(Branch).all()
    return showdata


@router.get('/{id}', response_model=schemas.BranchName)
def getdata(id, db: Session = Depends(get_db)):
    get_data = db.query(Branch).filter(Branch.id == id).first()
    if not get_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Branch with the id {id} not found")
    return get_data


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def updatedata(id, request: schemas.BranchName, db: Session = Depends(get_db)):
    get_branch_id = db.query(Branch).filter(Branch.id == id)
    print(get_branch_id)
    if not get_branch_id.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Branch with the id {id} not found")
    get_branch_id.update(request.dict())
    db.commit()
    return "updated"


@router.delete('/{id}')
def destroy(id, db: Session =  Depends(get_db)):
    branch_data_id = db.query(Branch).filter(Branch.id == id)
    if not branch_data_id.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Branch with the id {id} not found")
    branch_data_id.delete(synchronize_session=False)
    db.commit()
    return "Record Deleted from database.!!"