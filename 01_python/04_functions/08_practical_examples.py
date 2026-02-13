# LESSON 9: Practical Examples - All Concepts Together



# === Example: Shopping Cart ===
def calculate_total(price, quantity=1, discount=0, tax=0.15):
    """Calculates total with discount and tax."""
    subtotal = price * quantity
    after_discount = subtotal * (1 - discount/100)
    return round(after_discount * (1 + tax), 2)

print(f"Total: ${calculate_total(100, 3, discount=10)}")

# === Example: Grade Calculator ===
def get_grade(*scores):
    """Returns letter grade from average of scores."""
    avg = sum(scores) / len(scores)
    if avg >= 90: return "A"
    if avg >= 80: return "B"
    if avg >= 70: return "C"
    if avg >= 60: return "D"
    return "F"

print(f"Grade: {get_grade(85, 92, 78)}")

# === Example: User Profile ===
def create_profile(name, **details):
    """Creates profile from name and any extra details."""
    print(f"\n=== {name}'s Profile ===")
    for key, value in details.items():
        print(f"  {key}: {value}")

create_profile("Ali", age=25, city="Dubai", job="Engineer")

# === Summary ===
print("\n✅ You learned: def, parameters, return, defaults,")
print("   keyword args, *args, **kwargs, and docstrings!")
