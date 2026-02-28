from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from fastapi.responses import JSONResponse

class User(BaseModel):
    name: str
    email: str
    age: int
    password: str
    is_admin: bool

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Hello World"
    }

@app.put("/users/{user_id}", status_code=status.HTTP_200_OK)
def update_user(user_id: int, user:User):
    db_user_id = 45
    if user_id != db_user_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"message": "User not found"}
        )
    if user.password != "123456":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"message": "Your password is incorrect"}
        )
    if user.is_admin != True:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail={"message": "You are not authorized to update this user"}
        )
    return {
        "message": "User updated successfully",
        "user_id": user_id,
        "user": user
    }

@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user:User):
    return {
        "message": "User created successfully",
        "user": user
    }

@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    return {
        "message": "User deleted successfully",
        "user_id": user_id
    }