# models.py

from pydantic import BaseModel
from typing import Optional
import datetime
from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class UserBase(BaseModel):
    Name: Optional[str] = None
    Email: Optional[str] = None
    Password: str
    Role: Optional[int] = None

class UserCreate(UserBase):
    Name: str = None
    Email: str = None
    Password: str = None

class Usergggg(UserBase):
    UserID: int

    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    Name: Optional[str] = None
    Email: Optional[str] = None
    Password: Optional[str] = None
    Role: Optional[int] = None

class UserResponse(BaseModel):
    UserID: int
    Name: Optional[str] = None
    Email: Optional[str] = None
    Role: Optional[int] = None

    class Config:
        orm_mode = True

class NewId(BaseModel):
    code: int
    id: int

class InputUser(BaseModel):
    login: str
    password: str
    post_id: Optional[int] = None

class User(BaseModel):
    id: int
    login: Optional[str] = None
    reg_date: Optional[datetime] = None
    post_id: int
    post: Optional[str] = None

# class Post(BaseModel):
#     id: Optional[int] = None
#     name: str
