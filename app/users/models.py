from pydantic import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from database import Base


class User(Base):
    __tablename__ = "users"


    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)

    # user semester student back populate
    user_sem_subject = relationship('SemesterStudent', back_populates="sem_stu_user", lazy="joined")

    # user_sub_doc = relationship('SubjectDocument', back_populates="sem_stu_user", lazy="joined")