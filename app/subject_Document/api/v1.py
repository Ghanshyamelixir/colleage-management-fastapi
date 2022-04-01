from sqlalchemy.orm import Session
from database import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from app.subject_Document.models import SubjectDocument
from app.subject_Document import schemas
from app.subject.models import Subject
from app.users.models import User
from typing import List
from app.users.oauth import get_current_url
from app.users.schemas import UserCreate


route = APIRouter(
    prefix="/subjectDocument",
    tags=["subjectDocument"]
)


@route.post('/', response_model=schemas.SubjectDocumentDataId)
def sub_doc_create(request: schemas.SubjectDocumentCreate, db: Session = Depends(get_db),get_current_user:UserCreate = Depends(get_current_url)):
    subject_id = db.query(Subject).get(request.subject_id)
    user_id = db.query(User).get(request.user_id)

    sub_doc_create_data = SubjectDocument(subject_id=request.subject_id, user_id=request.user_id,
                                          filefield=request.filefield)
    db.add(sub_doc_create_data)
    db.commit()
    db.refresh(sub_doc_create_data)
    return sub_doc_create_data.__dict__


@route.get('/', response_model=List[schemas.SubjectDocumentGet])
def get_all_sub_doc_data(db: Session = Depends(get_db),get_current_user:UserCreate = Depends(get_current_url)):
    alldata = db.query(SubjectDocument).all()
    return alldata


@route.get('/{id}', response_model=schemas.SubjectDataId)
def get_data_using_id(id, db: Session = Depends(get_db),get_current_user:UserCreate = Depends(get_current_url)):
    getdata = db.query(SubjectDocument).filter(SubjectDocument.id == id).first()
    if not getdata:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"SubjectDocument with id {id} not found")
    return getdata


@route.put('/{id}')
def update_record(id, request: schemas.SubjectDocumentUpdate, db: Session = Depends(get_db), get_current_user:UserCreate = Depends(get_current_url)):
    updatedata = db.query(SubjectDocument).filter(SubjectDocument.id == id)
    if not updatedata:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"SubjectDocument with id {id} not found")
    updatedata.update(request.dict())
    db.commit()
    return "Record Updated Sucessfully"
