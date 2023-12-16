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

class User(UserBase):
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
    email: str
    password: str
    Role: Optional[int] = None
