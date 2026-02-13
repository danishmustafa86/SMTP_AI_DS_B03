# LESSON 2: Function Parameters (Inputs)
# Parameters let you pass data INTO a function

# === Without Parameter (fixed) ===
def greet_fixed():
    print("Hello, Ali!")

greet_fixed()  # Always same output

# === With Parameter (flexible) ===
def greet(name):  # 'name' is the PARAMETER
    print(f"Hello, {name}!")

greet("Ali")    # "Ali" is the ARGUMENT
greet("Sara")
greet("Ahmed")

# === More Examples ===
def double(num):
    print(f"{num} doubled is {num * 2}")

def is_adult(age):
    if age >= 18:
        print("Adult")
    else:
        print("Minor")

double(5)
is_adult(25)
is_adult(15)
