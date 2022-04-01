from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class SemesterStudent(Base):
    __tablename__ = 'semster_student'
    id = Column(Integer, primary_key=True, index=True)
    semester_id = Column(ForeignKey('semester.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

    # semester back populate
    sem_stu_semester = relationship('Semester', back_populates="sem_semester_student", lazy="joined")

    # user back populate
    sem_stu_user = relationship('User', back_populates="user_sem_subject", lazy="joined")
