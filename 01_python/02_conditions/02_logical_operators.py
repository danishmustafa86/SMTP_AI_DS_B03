"""Logical operators: and, or, not

We combine multiple conditions to make smarter decisions, like:
- "User is logged in AND has paid"
- "Age is under 12 OR over 60 for a discount"
- "NOT blocked_user"
"""

# AND: both conditions must be True
has_ticket = True
age = 15

print("Has ticket:", has_ticket)
print("Age:", age)
print("Can enter cinema (needs ticket AND age >= 13)?",
      has_ticket and age >= 13)

print("--------------------------------")

# OR: at least one condition must be True
is_student = True
is_senior = False

print("Is student:", is_student)
print("Is senior:", is_senior)
print("Gets discount (student OR senior)?",
      is_student or is_senior)

print("--------------------------------")

# NOT: reverses a True/False value
is_blocked_user = False

print("Is blocked user:", is_blocked_user)
print("Can user post comment? (NOT blocked)",
      not is_blocked_user)

print("--------------------------------")

# Real-world style example: free shipping rule
cart_total = 30
is_premium_member = True

# Free shipping if cart_total >= 50 OR user is a premium member
gets_free_shipping = cart_total >= 50 or is_premium_member

print("Cart total:", cart_total)
print("Is premium member:", is_premium_member)
print("Gets free shipping?", gets_free_shipping)


