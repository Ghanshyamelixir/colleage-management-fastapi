from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Semester(Base):
    __tablename__ = "semester"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    branch_id = Column(Integer, ForeignKey("branch.id"))


    # Branch Populate
    sem_branch = relationship('Branch', back_populates="branch_semester", lazy="joined")

    # subject relationship
    sem_subject = relationship('Subject',  back_populates="subject_semesters", lazy="joined")

    # sem_student back populate
    sem_semester_student = relationship('SemesterStudent', back_populates="sem_stu_semester", lazy="joined")

