
from typing import List
from Server.Users.models import User, UserCreate, NewId, InputUser, UserBase
from Server.db_manager import base_manager
from fastapi import HTTPException

def get_users() -> List[User]:
    res = base_manager.execute("SELECT UserID, Name, Email, Password, Role FROM Users", many=True)
    users = []
    for item in res['data']:
        user_data = {
            'UserID': item[0],
            'Name': item[1],
            'Email': item[2],
            'Password': item[3],
            'Role': item[4],
        }
        user = User(**user_data)
        users.append(user)
    return users


def add_user(new_user: UserCreate):
    res = base_manager.execute("INSERT INTO Users (Name, Email, Password, Role) "
                               "VALUES (?, ?, ?, ?) RETURNING UserID",
                               args=(new_user.Name, new_user.Email, new_user.Password, new_user.Role))
    return NewId(code=200, id=123)

def delete_user(user_id: str):
    res = base_manager.execute("DELETE FROM Users WHERE UserID = ?", args=(user_id))
    if res['code'] == 200:
        return NewId(code=res['code'],id=user_id)
    return None

def check_user(login: InputUser) -> User:
    res = base_manager.execute(
        "SELECT id, post_id FROM users WHERE login=? AND password=?",
        args=(login.login.lower(), login.password),
        many=False
    )
    print(res)
    if res['data']:
        return User(id=res['data'][0], post_id=res['data'][1])
    else:
        return User(id=0, post_id=0)
