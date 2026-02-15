from fastapi import FastAPI, Header
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()


class User(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    age: int = Field(..., ge=18, le=100)
    email: str = Field(..., format="email")


class UserUpdate(BaseModel):
    """All fields optional for PATCH (partial update)."""
    name: Optional[str] = Field(None, min_length=3, max_length=50)
    age: Optional[int] = Field(None, ge=18, le=100)
    email: Optional[str] = Field(None, format="email")


@app.get("/")
def home():
    return {"message": "Hello Ahmad"}

@app.get("/users")
def users(user_id: int , name: Optional[str] = "ali", is_yes:Optional[bool] = True, x_api_key: Optional[str] = Header(None)):  # use ?user_id=50 in the URL
    return {
        "message": "successfully fetched user",
        "user_id": user_id,
        "name": name,
        "is_yes":is_yes
    }

@app.get("/users/{user_id}/{name}")
def user_by_id(user_id: int, name:str):
    # GET only has path param; use /users/50 (no body)
    return {
        "user_id": user_id,
        "user_name": name,
        "user_age": 25,
        "user_email": "user@example.com"
    }

@app.post("/users")
def create_user(user:User, x_api_key: Optional[str] = Header(None), content_type: Optional[str] = Header(None), user_agent: Optional[str] = Header(None)):
    return {
        "name": user.name,
        "age": user.age,
        "email": user.email, 
        "x_api_key": x_api_key,
        "content_type": content_type,
        "user_agent": user_agent
    }

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User, x_api_key: Optional[str] = Header(None), content_type: Optional[str] = Header(None), user_agent: Optional[str] = Header(None)):
    return {
        "user_id": user_id,
        "name": user.name,  
        "age": user.age,
        "email": user.email, 
        "x_api_key": x_api_key,
        "content_type": content_type,
        "user_agent": user_agent
    }

@app.patch("/users/{user_id}")
def patch_user(user_id: int, user: UserUpdate, x_api_key: Optional[str] = Header(None), content_type: Optional[str] = Header(None), user_agent: Optional[str] = Header(None)):
    # Only include fields that were sent (not None)
    return {
        "user_id": user_id,
        "updated_fields": user.model_dump(exclude_unset=True),
        "x_api_key": x_api_key,
        "content_type": content_type,
        "user_agent": user_agent
    }