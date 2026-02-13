# LESSON 3: Return Values
# Use 'return' to get a value back from a function

# === print vs return ===
def add_print(a, b):
    print(a + b)  # Shows on screen, returns None

def add_return(a, b):
    return a + b  # Gives value back

x = add_print(3, 5)   # Shows 8, but x = None
y = add_return(3, 5)  # Nothing shown, y = 8
print(f"x = {x}, y = {y}")

# === Why Return is Useful ===
def multiply(a, b):
    return a * b

result = multiply(4, 5)
print(f"Result: {result}")

# Use in calculations
total = multiply(3, 4) + multiply(2, 5)
print(f"Total: {total}")

# === Different Return Types ===
def is_even(n):
    return n % 2 == 0

print(f"Is 10 even? {is_even(10)}")
print(f"Is 7 even? {is_even(7)}")

# === Return Stops Function ===
def check_age(age):
    if age < 0:
        return "Invalid age"
    if age >= 18:
        return "Adult"
    return "Minor"

print(check_age(-5))
print(check_age(25))
print(check_age(10))
