# Status Codes
# Exception Handling.

from fastapi import FastAPI , status
from fastapi.responses import JSONResponse



app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/users/{user_id}/{age}", status_code=status.HTTP_200_OK)
def get_user(user_id: int, age: int):
    if age < 18:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "User must be 18 or older"
        )
    if user_id != 20:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
            )
    return {
        "user_id": user_id,
        "name": "Ahmad",
        "email": "ahmad@gmail.com",
        "age": 20
    }


