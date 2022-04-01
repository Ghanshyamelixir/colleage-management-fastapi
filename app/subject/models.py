from sqlalchemy import Integer, String, Column, ForeignKey
from database import Base
from sqlalchemy.orm import relationship


class Subject(Base):
    __tablename__ = "subject"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    semester_id = Column(Integer, ForeignKey('semester.id'))

    #semester back-populate
    subject_semesters = relationship('Semester', back_populates="sem_subject", lazy="joined")

    # subject Document back-populate
    subject_sub_doc = relationship("SubjectDocument", back_populates="sub_doc_subject", lazy="joined")



