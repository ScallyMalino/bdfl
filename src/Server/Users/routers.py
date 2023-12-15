from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import FastAPI
from typing import List
from Server.Users.models import User, UserCreate, NewId , InputUser
from Server.Users.resolvers import get_users, add_user, delete_user, check_user

router = APIRouter()

@router.get('/check')
def check_exists_user(user: InputUser) -> User:
    return check_user(user)

@router.get('/get/', response_model=List[User])
def get_users_endpoint():
    return get_users()

@router.post('/post/', response_model=NewId)
def add_user_endpoint(new_user: UserCreate):
    return add_user(new_user)

@router.delete("/delete/{user_id}")
def delete_group(user_id: str) -> NewId:
    return delete_user(user_id)


