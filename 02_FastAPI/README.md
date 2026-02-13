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

