from database import Base, engine
from app.branch import models
from app.sem import models
from app.sem_Student import models
from app.subject import models
from app.subject_Document import models
from app.users import models

Base.metadata.create_all(engine)