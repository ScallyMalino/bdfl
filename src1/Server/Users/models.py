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

class User1(UserBase):
    UserID: int

    class Config:
        orm_mode = True

# class User(BaseModel):
#     Userid: int
#     email: Optional[str] = None
#     password: Optional[str] = None
#     Role: int
#     post: Optional[str] = None
class User(BaseModel):
    Userid: Optional[int] = None
    email: Optional[str] = None
    password: Optional[str] = None
    Role: Optional[int] = None
    post: Optional[str] = None


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

class Post(BaseModel):
    id: Optional[int] = None
    name: str
class InputUser(BaseModel):
    Email: str
    Password: str
    Role: Optional[int] = None
