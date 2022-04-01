from fastapi import FastAPI

from app.branch.api.v1 import router
from app.sem.api.v1 import router as semroute
from app.subject.api.v1 import router as subjectroute
from app.users.api.v1 import route as userroute
from app.sem_Student.api.v1 import route as semesterstudent
from app.subject_Document.api.v1 import route as subjectdocument

from database import engine, Base
from app.sem import models as semester_model
from app.branch import models as branch_model
from app.sem_Student import models as sem_student_model
from app.subject import models as subject_model
from app.subject_Document import models as subject_document_model
from app.users import models as user_model

app = FastAPI()

sem_student_model.Base.metadata.create_all(bind=engine)
subject_model.Base.metadata.create_all(bind=engine)
user_model.Base.metadata.create_all(bind=engine)
subject_document_model.Base.metadata.create_all(bind=engine)
semester_model.Base.metadata.create_all(bind=engine)
branch_model.Base.metadata.create_all(bind=engine)



app.include_router(router)
app.include_router(semroute)
app.include_router(subjectroute)
app.include_router(userroute)
app.include_router(semesterstudent)
app.include_router(subjectdocument)
