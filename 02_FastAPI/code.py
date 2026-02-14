from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()



class User(BaseModel):
    name: str
    email: str
    age: int




@app.get("/")
def home_route():
    return {"message": "Hello Ahmad"}

@app.get("/users")
def Get_users():
    return {"Users": ["Ahmad", "Ali", "Hamza"]}

@app.get("/users/{user_id}")
def Get_user(user_id: int):
    return {
        "user_id": user_id,
        "name": "Ahmad",
        "email": "ahmad@gmail.com",
        "age": 20
        }

@app.get("/users/{user_id}/profile")
def Get_user_profile(user_id: int):
    return {
        "user_id": user_id,
        "name": "ali",
        "email": "ahmad@gmail.com",
        "age": 20
        }
@app.post("/users")
def Create_user(user: User):
    return {"user": user}

@app.put("/users/{user_id}")
def Update_user(user_id: int, user: User):
    return {
        "user_id": user_id,
        "name": user.name,
        "email": user.email,
        "age": user.age
        }
@app.delete("/users")
def Delete_user(user_id: int, user: User):
    return {
        "message": "User deleted successfully",
        "user_id": user_id,
        "name": user.name,
        "email": user.email,
        "age": user.age
        }

