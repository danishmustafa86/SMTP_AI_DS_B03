from fastapi import FastAPI
from pydantic import BaseModel

danish =FastAPI()


class User(BaseModel):
    name: str
    email: str
    age: int



@danish.get("/")
def home_route():
    return {"message": "Hello Ahmad"}

@danish.patch("/users/{user_id}")
def update_user(user_id: int, user: User, gender: str = "male" | "female" | "other"):
    return {
        "user_id": user_id,
        "name": user.name,
        "email": user.email,
        "age": user.age
    }