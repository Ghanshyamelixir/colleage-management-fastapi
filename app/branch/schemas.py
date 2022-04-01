from pydantic import BaseModel



class Branch(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class BranchNameResponse(BaseModel):
    name: str


class BranchName(BaseModel):
    name: str

    class Config:
        orm_mode = True



class Branchupdate(BaseModel):
    id: int
    name: str
