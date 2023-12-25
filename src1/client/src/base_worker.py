import datetime
import requests
import json


class BaseWorker:

    def __init__(self, server_url: str):
        self.server_url = server_url
        self.end_points = {"check_login": self.server_url + "/users/check",
                           "users": self.server_url + "/users/get",
                           "posts": self.server_url + "/users/posts",
                      }

    def check_user_login(self, user: "User") -> "Login":
        resp = requests.get(url=self.end_points.get('check_login'), json=user.to_json())
        print("JSON response from server:", resp.json())
        return Login(Email=resp.json().get('Email'), Password=resp.json().get('password'))

    def get_users_list(self):
        resp = requests.get(url=self.end_points.get('users'))
        return [User(UserID=user['UserID'], Name=user['name'], Email=user['email'], password=user['password'], Role=user['Role'])
                for user in resp.json()]

    def get_posts_list(self):
        resp = requests.get(url=self.end_points.get('posts'))
        return [Post(id=post['id'], name=post['name']) for post in resp.json()]

class Login:
    def __init__(self, Email: str, Password: str, Role: int = 1):
        self.Email = Email
        self.Password = Password
        self.Role = Role

class User:
    def __init__(self, Email: str, post: str = None, UserID: int = None, Role: int = 0,
                 password: str = None, Name: str = None):
        self.UserID = UserID
        self.Name = Name
        self.Email = Email
        self.post = post
        self.Role = Role
        self.password = password

    def to_json(self):
        return {
            "Email": self.Email,
            "password": self.password,
            "Role": self.Role
        }
class Post:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name