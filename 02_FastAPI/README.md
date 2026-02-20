# 🧠 FastAPI 

## 🎯 Objective 

> “Today we will understand **why FastAPI exists**, **what problems it solves**, **how it works internally**, and then build **very small APIs** to understand **Path, Query, and Body parameters**.”


---

## 1️⃣ What Problem Exists Before FastAPI? (VERY IMPORTANT)


> Imagine you are building a backend for:

* a mobile app
* a website
* an AI system

They all need to **talk to the server**.

### Old problems:

* Writing APIs was **slow**
* Validation had to be written **manually**
* Documentation was written **separately**
* Errors appeared **at runtime**
* Performance was not great

👉 Backend development felt **heavy and messy**.

---

## 2️⃣ What is FastAPI? (Core Definition)

### Say this clearly:

> **FastAPI is a modern Python framework used to build APIs easily, safely, and very fast.**

Break the name:

* **Fast** → High performance (almost like Node.js)
* **API** → Built only for APIs
* **Python** → Simple, readable, beginner-friendly

---

## 3️⃣ Why Do We Need FastAPI? (Problems It Solves)

### FastAPI solves 5 BIG problems:

---

### 🔴 Problem 1: Manual Validation

Before:

```python
if type(age) != int:
    return error
```

With FastAPI:

```python
age: int
```

✔ Automatic validation
✔ Less bugs
✔ Cleaner code

---

### 🔴 Problem 2: No API Documentation

Before:

* Use Postman
* Write docs separately

With FastAPI:

* `/docs` auto-generated
* Interactive UI
* No extra work

---

### 🔴 Problem 3: Slow Performance

FastAPI:

* Built on **Starlette** + **ASGI**
* Handles many requests efficiently
* Used in AI & production systems

---

### 🔴 Problem 4: Confusing Code

FastAPI:

* Uses **Python type hints**
* Code explains itself
* Easy to read for teams

---

### 🔴 Problem 5: Runtime Errors

FastAPI:

* Catches errors **before execution**
* Gives clear error messages

---

## 4️⃣ Why FastAPI is Better Than Competitors?

### Compare Simply (NO HATE 😄)

| Feature        | Flask  | Django | FastAPI   |
| -------------- | ------ | ------ | --------- |
| Speed          | Medium | Slow   | ⚡ Fast    |
| Validation     | Manual | Heavy  | Automatic |
| Docs           | Manual | Manual | Auto      |
| Learning Curve | Easy   | Hard   | Easy      |
| Modern APIs    | ❌      | ❌      | ✅         |

### Teaching Line:

> Flask is simple, Django is powerful, **FastAPI is modern**.

---

## 5️⃣ How FastAPI Works Internally (Conceptual)

### Explain like this:

1. User sends **request**
2. FastAPI:

   * reads URL
   * checks parameters
   * validates data
3. Your function runs
4. FastAPI converts output to JSON
5. Sends **response**

👉 You write **logic**, FastAPI handles **everything else**.

---

## 6️⃣ Your First FastAPI App (Hello World)

Now move to code 👇

### `main.py`

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello FastAPI"}
```

### Explain line-by-line:

* `FastAPI()` → create application
* `@app.get("/")` → API endpoint
* `def home()` → function runs when URL is called
* return → JSON response

---

### Run:

```bash
uvicorn main:app --reload
```

Explain:

* `uvicorn` → server
* `main` → file name
* `app` → FastAPI object
* `--reload` → auto restart

---

## 7️⃣ Swagger UI (Why This Is Powerful)

Open:

```
/docs
```

### Say this:

> This documentation is created **from our code automatically**.
> This saves **hours of work** in real companies.

Explain lightly:

* Test APIs
* See parameters
* Send data

---

## 7.5️⃣ FastAPI HTTP Methods (Quick Overview)

Before diving into parameters, understand **which HTTP method** each endpoint uses.

### Common methods:

| Method   | Use case              | Example              |
| -------- | ---------------------- | -------------------- |
| **GET**  | Read / fetch data      | Get user, list items |
| **POST** | Create new resource    | Signup, add item     |
| **PUT**  | Replace entire resource| Update user fully    |
| **PATCH**| Update part of resource| Change one field     |
| **DELETE** | Remove resource     | Delete user, item    |

### Little code examples:

```python
from fastapi import FastAPI

app = FastAPI()

# GET — read data (no body)
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

# POST — create (data in body)
@app.post("/users")
def create_user(name: str, age: int):
    return {"created": name, "age": age}

# PUT — replace whole resource
@app.put("/users/{user_id}")
def replace_user(user_id: int, name: str):
    return {"user_id": user_id, "name": name}

# PATCH — update only some fields
@app.patch("/users/{user_id}")
def update_user(user_id: int, name: str = None):
    return {"user_id": user_id, "updated": name}

# DELETE — remove resource
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    return {"deleted": user_id}
```

### Teaching line:

> **GET** = read, **POST** = create, **PUT** = replace all, **PATCH** = update part, **DELETE** = remove.

---

# ⭐ CORE DAY-1 CONCEPT ⭐

## Understanding Parameters (DEEP + SIMPLE)

---

## 8️⃣ Path Parameters (Deep Understanding)

### Concept:

> **Path parameters identify a specific resource**

### Real-life analogy:

* CNIC number
* Roll number
* User ID

---

### Code:

```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
```

### Explain deeply:

* `{user_id}` → value must come from URL
* `int` → FastAPI checks type
* Function only runs if data is valid

### Try:

```
/users/5
/users/abc ❌
```

---

## 9️⃣ Query Parameters (Deep but Simple)

### Concept:

> **Query parameters are used for filtering or searching**

### Example:

```
/search?item=phone
```

### Code:

```python
@app.get("/search")
def search(item: str):
    return {"item": item}
```

### Explain:

* Query params are **optional by nature**
* Used for search, filters, pagination

---

### Optional Query Parameter:

```python
from typing import Optional

@app.get("/products")
def products(category: Optional[str] = None):
    return {"category": category}
```

Explain:

> Optional means user **may or may not** send it.

---

## 🔟 Body Parameters (Most Confusing → Explain Slowly)

### Concept:

> **Body parameters are used when client sends structured data (JSON)**

### Real-life:

* Signup form
* Login form
* Payment info

---

### Pydantic Model:

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
```

Explain:

* This is NOT database
* This is **data shape**
* FastAPI validates automatically

---

### POST API:

```python
@app.post("/users")
def create_user(user: User):
    return user
```

Explain:

* POST → create
* Data goes in **body**
* Not visible in URL

---

## 1️⃣1️⃣ FINAL & MOST IMPORTANT COMPARISON

### Write this clearly on board:

| Parameter | Purpose           | Where     |
| --------- | ----------------- | --------- |
| Path      | Identify resource | URL       |
| Query     | Filter/search     | After `?` |
| Body      | Send data         | JSON      |

### Golden Sentence (Repeat):

> **Path identifies, Query filters, Body sends data**

---

## Answer these questions



* Get user by ID? → **Path**
* Search product? → **Query**
* Register user? → **Body**





> “FastAPI removes pain from backend development.
> Once parameters are clear, everything else is easy.”

---

# Advanced Topics (In-Depth with Code Examples)

The following sections cover **Pydantic Validation**, **Optional Parameters**, **Status Codes**, and **Exception Handling** in full detail with runnable examples.

---

## 1️⃣ Pydantic Validation (Deep Dive)

### What is Pydantic?

**Pydantic** is the data validation library that FastAPI uses under the hood. Every time you use a **Pydantic model** as a type (e.g. in the request body), FastAPI:

- Validates incoming JSON against the model
- Converts types (e.g. string to int where needed)
- Returns **422 Unprocessable Entity** with clear error messages if validation fails

You don’t write `if type(x) != int` — you define the **shape** and Pydantic does the rest.

### Basic model (data shape)

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    age: int
```

- `BaseModel` → class that describes the structure of your data.
- Each attribute has a type; Pydantic checks and coerces values.

Usage in an endpoint:

```python
@app.post("/users")
def create_user(user: User):
    return {"created": user.name, "age": user.age}
```

If the client sends `{"name": "Ahmad", "email": "a@b.com", "age": "25"}`, Pydantic will coerce `"25"` to `25`. If they send `{"name": "Ahmad"}` (missing `email`, `age`), FastAPI returns 422 with a list of validation errors.

### Field() — constraints and metadata

Use `Field()` to add validation rules and documentation:

```python
from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    email: str = Field(min_length=5, max_length=50)
    age: int = Field(gt=0, lt=150)
```

Common `Field()` arguments:

| Argument     | Meaning              | Example                    |
| ----------- | -------------------- | -------------------------- |
| `min_length`| Min length (str)     | `Field(min_length=1)`      |
| `max_length`| Max length (str)     | `Field(max_length=100)`    |
| `gt`        | Greater than (number)| `Field(gt=0)`              |
| `ge`        | Greater or equal     | `Field(ge=0)`              |
| `lt`        | Less than            | `Field(lt=150)`            |
| `le`        | Less or equal        | `Field(le=120)`            |
| `default`   | Default value        | `Field(default="N/A")`     |
| `description` | Shown in OpenAPI   | `Field(description="User age")` |

Example with defaults and description:

```python
class Product(BaseModel):
    name: str = Field(..., min_length=1, description="Product name")
    price: float = Field(gt=0, description="Price in USD")
    in_stock: bool = Field(default=True, description="Available for sale")
```

`...` means the field is **required** (no default).

### EmailStr and other specialized types

For emails, use `EmailStr` so Pydantic validates email format:

```python
from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    name: str = Field(max_length=100)
    email: EmailStr = Field(max_length=50)  # Must be valid email format
    age: int = Field(gt=0, lt=50)
```

Other useful types: `HttpUrl`, `IPv4Address`, `UUID`, `PositiveInt`, `NonNegativeFloat`, etc. They all integrate with FastAPI and appear in `/docs`.

### Optional fields in Pydantic

A field is optional if it has a default (e.g. `None`):

```python
from typing import Optional
from pydantic import BaseModel, Field

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    age: Optional[int] = None
```

So for PATCH you can send only the fields you want to change; the rest stay `None`.

### Complete validation example

```python
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field

app = FastAPI()

class User(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    email: EmailStr = Field(max_length=50)
    age: int = Field(gt=0, lt=150)

@app.post("/users")
def create_user(user: User):
    return {"message": "User valid", "data": user.model_dump()}
```

Invalid payloads (wrong types, missing required fields, invalid email, age out of range) will result in **422** and a JSON body listing the validation errors.

---

## 2️⃣ Optional Parameters (In-Depth)

### What “optional” means

- **Required:** Caller must provide the value; otherwise FastAPI returns 422.
- **Optional:** Caller may omit it; the default is used (often `None`).

In FastAPI, “optional” is implemented by giving the parameter a **default value**.

### Optional query parameters

```python
from typing import Optional

@app.get("/products")
def list_products(
    category: Optional[str] = None,
    min_price: Optional[float] = None,
    limit: Optional[int] = 10
):
    return {
        "category": category,
        "min_price": min_price,
        "limit": limit
    }
```

- `category` and `min_price`: may be omitted → `None`.
- `limit`: optional with default `10`; if omitted, `limit` is `10`.

Try:

- `/products` → all defaults.
- `/products?category=books` → filter by category.
- `/products?limit=5` → limit 5.

### Optional path parameters (rare)

Path parameters are usually required (they’re part of the URL). If you need “optional path-like” behavior, you typically use **query** parameters or two routes (e.g. `/items` and `/items/{id}`).

### Optional body fields (Pydantic)

Already shown above: use `Optional[str] = None` (or other type) in the model for fields that the client may omit.

### Optional headers

```python
from fastapi import Header

@app.get("/secure")
def secure(x_api_key: Optional[str] = Header(None)):
    if x_api_key is None:
        return {"message": "No API key provided"}
    return {"message": "Key received", "key_prefix": x_api_key[:4]}
```

### Summary

| Location   | Required                     | Optional                          |
| ---------- | ---------------------------- | --------------------------------- |
| Query      | `item: str`                  | `item: Optional[str] = None`      |
| Body field | `name: str` in model         | `name: Optional[str] = None`      |
| Header     | `x_key: str = Header()`      | `x_key: Optional[str] = Header(None)` |

---

## 3️⃣ Status Codes (Full Coverage)

### Why status codes matter

HTTP status codes tell the client:

- **2xx** — Success (e.g. 200 OK, 201 Created).
- **4xx** — Client error (e.g. 400 Bad Request, 404 Not Found).
- **5xx** — Server error (e.g. 500 Internal Server Error).

FastAPI lets you set the status code per endpoint and when raising exceptions.

### Setting status code on success

Use the `status_code` argument of the decorator:

```python
from fastapi import FastAPI, status

app = FastAPI()

@app.get("/", status_code=status.HTTP_200_OK)
def home():
    return {"message": "Hello World"}

@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    return {"message": "User created", "data": user}

@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    # No body for 204; just return or return None
    return None
```

### Common status code constants

| Constant                         | Code | When to use                    |
| -------------------------------- | ---- | ------------------------------ |
| `HTTP_200_OK`                    | 200  | GET success, general OK       |
| `HTTP_201_CREATED`               | 201  | POST created a resource        |
| `HTTP_204_NO_CONTENT`            | 204  | DELETE success, no body        |
| `HTTP_400_BAD_REQUEST`           | 400  | Invalid request (e.g. bad data)|
| `HTTP_401_UNAUTHORIZED`          | 401  | Not authenticated              |
| `HTTP_403_FORBIDDEN`             | 403  | Authenticated but not allowed  |
| `HTTP_404_NOT_FOUND`             | 404  | Resource not found             |
| `HTTP_405_METHOD_NOT_ALLOWED`    | 405  | Wrong HTTP method              |
| `HTTP_422_UNPROCESSABLE_ENTITY`  | 422  | Validation error (auto by FastAPI) |
| `HTTP_500_INTERNAL_SERVER_ERROR` | 500  | Unexpected server error        |

Using numeric codes is possible but not recommended:

```python
@app.get("/", status_code=200)
def home():
    return {"message": "OK"}
```

Prefer `status.HTTP_200_OK` for clarity and refactoring.

### Returning a custom status code (e.g. Response)

For full control (e.g. different status per branch), use `JSONResponse`:

```python
from fastapi.responses import JSONResponse

@app.post("/users")
def create_user(user: User):
    if user.age < 18:
        return JSONResponse(
            status_code=400,
            content={"detail": "User must be 18 or older"}
        )
    # Normal creation
    return JSONResponse(
        status_code=201,
        content={"message": "User created", "data": user.model_dump()}
    )
```

### Status code with HTTPException (next section)

When you **raise** an error, you set the status code on `HTTPException`; that overrides the default success `status_code` of the route for that response path.

---

## 4️⃣ Exception Handling (In-Depth)

### HTTPException — controlled client/server errors

FastAPI’s `HTTPException` is the standard way to return a non-2xx response with a JSON body:

```python
from fastapi import FastAPI, HTTPException, status

@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = find_user_by_id(user_id)  # Your logic
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user
```

- **status_code:** HTTP status (e.g. 404, 400, 403).
- **detail:** Message (string or dict) shown in the response body under `"detail"`.

Example response when user not found:

```json
{
  "detail": "User not found"
}
```

### Adding custom headers with HTTPException

```python
raise HTTPException(
    status_code=403,
    detail="Access denied",
    headers={"X-Error-Code": "FORBIDDEN_RESOURCE"}
)
```

### Global exception handlers

You can catch **all** instances of a given exception type and return a consistent format.

Signature: `(request, exc)` → return a `Response` (e.g. `JSONResponse`).

#### Handling HTTPException

```python
from fastapi import Request
from fastapi.responses import JSONResponse

@app.exception_handler(HTTPException)
def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )
```

Now every `raise HTTPException(...)` is converted to this JSON shape (you can change the shape if you want, e.g. add `"error": True`).

#### Handling a specific HTTP status (e.g. 405)

You can register a handler for a **status code** (integer) to catch responses that would return that code:

```python
@app.exception_handler(405)
def method_not_allowed_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=405,
        content={"detail": "This method is not allowed here."}
    )
```

So when FastAPI would return 405 (e.g. POST to a path that only allows GET), your custom message is sent instead.

#### Handling generic Exception (500)

For unhandled Python exceptions (to avoid leaking stack traces and to return a stable format):

```python
@app.exception_handler(Exception)
def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "An internal error occurred."}
    )
```

In production you might log `exc` and use a generic message only in the response.

### Order of handlers

FastAPI uses the **most specific** handler first. So if both `HTTPException` and `Exception` are registered, for `raise HTTPException(...)` the `HTTPException` handler is used.

### Full example: validation + optional + status codes + exceptions

```python
from fastapi import FastAPI, HTTPException, status, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

app = FastAPI()

class User(BaseModel):
    name: Optional[str] = Field(default=None, max_length=100)
    email: EmailStr = Field(max_length=50)
    age: int = Field(gt=0, lt=150)

@app.exception_handler(HTTPException)
def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )

@app.get("/", status_code=status.HTTP_200_OK)
def home():
    return {"message": "Hello World"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
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

@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    return {
        "message": "User created successfully",
        "data": user.model_dump()
    }

@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    return None
```

---

## Quick reference

| Topic                 | Main idea                                                                 |
| --------------------- | ------------------------------------------------------------------------- |
| **Pydantic Validation** | Define models with types and `Field()`; FastAPI validates and returns 422 on failure. |
| **Optional Parameters** | Use `Optional[T] = None` or other default for query/body/header so the client can omit. |
| **Status Codes**      | Set `status_code=status.HTTP_XXX` on the route or in `HTTPException` / `JSONResponse`. |
| **Exception Handling**| Use `raise HTTPException(...)` for control flow; use `@app.exception_handler` for global format. |

