from fastapi import FastAPI , status
from pydantic import BaseModel, Field, EmailStr
from typing import Optional

app = FastAPI()


class User(BaseModel):
    name: Optional[str] = Field(default=  "danish" ,min_length=3, max_length=100)
    email: EmailStr = Field(max_length=50)
    age: int = Field(gt=0, lt=50)

@app.get("/", status_code=status.HTTP_200_OK)
def home():
    return {"message": "Hello World"}


@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: User, user_id: Optional[int] = 555):
    return {
        "message": "User created successfully",
        "user_id": user_id,
        "email": user.email,
        "age": user.age,
        "name": user.name,
    }

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    return {
        "message": "User deleted successfully",
        "user_id": user_id,
    }
