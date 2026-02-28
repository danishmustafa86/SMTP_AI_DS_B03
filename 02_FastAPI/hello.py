from fastapi import FastAPI, Request, status, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


class User(BaseModel):
    name: str
    email: str
    age: int

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)



@app.get("/")
def home():
    return {"message": "Hello World"}


@app.get("/users/{user_id}", status_code = status.HTTP_200_OK)
def get_user(user_id: int):
    if user_id != 20:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found here")
    return {"message": "User found", "user_id": user_id}

@app.post("/users", status_code = status.HTTP_201_CREATED)
def create_user(user: User):
    if user.age < 18:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User must be 18 or older")
    if user.email != "ahmad@gmail.com":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email must be ahmad@gmail.com")
    if user.name != "Ahmad":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Name must be Ahmad")
    if user.age != 20:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Age must be 20")
    return {"message": "User created", "user": user}


@app.exception_handler(HTTPException)
def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code = exc.status_code, 
        content = {"Detail": exc.detail},
        headers = {"X-Error-Code": "FORBIDDEN_RESOURCE"}
    )