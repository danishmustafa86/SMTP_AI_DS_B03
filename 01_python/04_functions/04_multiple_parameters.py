# LESSON 4: Multiple Parameters
# Separate parameters with commas

# === Two Parameters ===
def greet(name, greeting):
    print(f"{greeting}, {name}!")

greet("Ali", "Hello")
greet("Sara", "Welcome")

# === Order Matters! ===
def introduce(name, age, city):
    print(f"{name}, {age} years old, from {city}")

introduce("Mohammad", 25, "Riyadh")  # Correct
introduce(25, "Riyadh", "Mohammad")  # Wrong order!

# === With Return ===
def rectangle_area(length, width):
    return length * width

def calculate_bmi(weight, height):
    return weight / (height ** 2)

print(f"Area: {rectangle_area(10, 5)}")
print(f"BMI: {calculate_bmi(70, 1.75):.1f}")

# === Grade Calculator ===
def calculate_grade(midterm, final, assignments):
    return (midterm * 0.3) + (final * 0.5) + (assignments * 0.2)

score = calculate_grade(85, 90, 95)
print(f"Final score: {score}")
