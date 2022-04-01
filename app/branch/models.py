from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship

from database import Base


class Branch(Base):
    __tablename__ = "branch"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    branch_semester = relationship('Semester', back_populates="sem_branch")
