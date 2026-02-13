# LESSON 5: Default Parameters (Optional)
# Set default values with = after parameter

# === Basic Default ===
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Ali", "Hi")   # Uses "Hi"
greet("Sara")        # Uses default "Hello"

# === Multiple Defaults ===
def make_coffee(size="medium", milk=True, sugar=2):
    milk_text = "with milk" if milk else "black"
    print(f"{size} coffee, {milk_text}, {sugar} sugars")

make_coffee()                    # All defaults
make_coffee("large")             # Change size only
make_coffee("small", False, 0)   # Change all

# === Rule: Defaults Must Come Last ===
# WRONG: def bad(name="John", age):
# CORRECT:
def good(age, name="John"):
    print(f"{name} is {age}")

good(25, "Ali")
good(30)  # Uses default name

# === Practical Example ===
def power(base, exponent=2):
    return base ** exponent

print(f"5² = {power(5)}")
print(f"2³ = {power(2, 3)}")
