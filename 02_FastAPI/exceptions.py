from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel

app = FastAPI()

# -----------------------------
# 1️⃣ Sample Pydantic Model
# -----------------------------

class User(BaseModel):
    name: str
    age: int


# -----------------------------
# 2️⃣ Normal Route
# -----------------------------

@app.get("/")
def home():
    return {"message": "API is running"}


# -----------------------------
# 3️⃣ Route with HTTPException
# -----------------------------

@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id != 1:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user_id": user_id}


# -----------------------------
# 4️⃣ Route that causes Python error
# -----------------------------

@app.get("/divide")
def divide(a: int, b: int):
    return {"result": a / b}  # if b=0 → ZeroDivisionError


# -----------------------------
# 5️⃣ Route with Validation
# -----------------------------

@app.post("/create-user")
def create_user(user: User):
    return {"message": "User created", "data": user}


# -----------------------------
# 6️⃣ Custom Exception
# -----------------------------

class BalanceTooLow(Exception):
    def __init__(self, balance):
        self.balance = balance


@app.get("/withdraw")
def withdraw(balance: int, amount: int):
    if amount > balance:
        raise BalanceTooLow(balance)
    return {"message": "Withdrawal successful"}


# -----------------------------
# 7️⃣ Custom Exception Handler
# -----------------------------

@app.exception_handler(BalanceTooLow)
async def balance_exception_handler(request: Request, exc: BalanceTooLow):
    return JSONResponse(
        status_code=400,
        content={
            "success": False,
            "error": f"Your balance is only {exc.balance}"
        }
    )


# -----------------------------
# 8️⃣ Validation Error Handler
# -----------------------------

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "success": False,
            "message": "Invalid input data",
            "errors": exc.errors()
        }
    )


# -----------------------------
# 9️⃣ Global Exception Handler
# -----------------------------

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": "Something went wrong",
            "error": str(exc)
        }
    )