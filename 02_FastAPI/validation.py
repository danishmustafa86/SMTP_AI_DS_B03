from fastapi import FastAPI, status, Request
fron fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr, Field
from typing import Optional


app = FastAPI()

class User(BaseModel):
    name: Optional[str] = Field(default = None, min_length=0, max_length=10)
    email: EmailStr = Field(min_length=0, max_length=50)
    age: int = Field(gt=0, lt=50)


@app.exception_handler(HTTPException)
def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )

@app.exception_handler(405)
def custom_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=status.HTTP_405_NOT_FOUND,
        content={"detail": "This method is not allowed here."}
    )


@app.get("/", status_code=status.HTTP_200_OK)
def home():
    return {"message": "Hello World"}


age = 20

@app.get("/users/{user_id}")
def get_user(user_id:int):
    if user_id != age:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = "User not found"
            )
    return {
        "user_id": user_id,
        "name": "Ahmad",
        "email": "ahmad@gmail.com",
        "age": 20
    }


# using exception handler 405
@app.post("/users", status_code=status.HTTP_405_METHOD_NOT_ALLOWED)
def create_user(user:User):
    return {
        "status_code": status.HTTP_405_METHOD_NOT_ALLOWED,
        "message": "This method is not allowed here."
    }


@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user:User):
    return {
        "status_code": status.HTTP_201_CREATED,
        "message": "User created successfully",
        "data": user
    }

@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id:int):
    print(user_id)









@app.get("/users/{user_id}")
def update_user(user_id:int, is_active:bool):
    return {
        "user_id": user_id,
        "is_active": is_active
    }