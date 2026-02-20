from fastapi import FastAPI, Header
from typing import Optional
from pydantic import BaseModel


app = FastAPI()


class User(BaseModel):
    name: str
    email: str
    age: int


class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    age: Optional[int] = None


@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id,
        "name": "Ahmad",
        "email": "ahmad@gmail.com",
        "age": 20
    }

@app.get("/users")
def get_users(name: Optional[str] = None, age: Optional[int] = None, email: Optional[str] = None):


    return {
        "name": name,
        "age": age,
        "email": email
    }


@app.post("/users")
def create_user(user:User, x_api_key:str = Header(None)):
    return 
    {
        "name": user.name,
        "age": user.age,
        "email": user.email, 
        "x_api_key": x_api_key,
    }

@app.patch("/users/{user_id}")
def update_user(user_id:int, user:UserUpdate, x_api_key:str = Header(None), content_type:str = Header(None)):
    return 
    {
        "user_id": user_id,
        "name": user.name,
        "age": user.age,
        "email": user.email, 
        "x_api_key": x_api_key,
    }