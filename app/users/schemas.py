from pydantic import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from fastapi import Depends
from typing import Optional

class User(BaseModel):
    id : int
    email : str
    hashed_password : str


    class Config:
        orm_mode = True


class UserResponse(BaseModel):
    email : str
    hashed_password : str


class UserCreate(BaseModel):
    email: str
    hashed_password : str


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None