from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from fastapi import FastAPI, File, Form, UploadFile

app = FastAPI()

class SubjectDocument(Base):
    __tablename__ = "subject_document"

    id = Column(Integer, primary_key=True, index=True)
    subject_id = Column(Integer, ForeignKey('subject.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

    # Subject File back populate
    sub_doc_subject = relationship('Subject', back_populates="subject_sub_doc", lazy="joined")

    # user back populate
    # sub_doc_user = relationship('User', back_populates="user_sub_doc", lazy="joined")
    filefield = Column(String)

# @app.post("/uploadfile/", status_code=201)
# async def create_upload_file(properties: SubjectDocument, file: UploadFile = File(...)):
#     return {"filename": file.filename, 'properties': properties}
