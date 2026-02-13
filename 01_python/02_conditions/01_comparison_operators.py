"""Comparison operators: we use them to ask questions like
"Is the user old enough?", "Is the payment complete?", or
"Is the temperature higher than 30 degrees?".

This file shows basic examples of:
- ==  (equal to)
- !=  (not equal to)
- >, <, >=, <=  (greater/less than)
"""

# Check if two values are equal
age = 18
required_age = 18

print("Age:", age)
print("Required age:", required_age)
print("Is age equal to required age?", age == required_age)

print("--------------------------------")

# Check if values are different
password_from_user = "secret123"
correct_password = "secret123"

print("Is password different from correct_password?",
      password_from_user != correct_password)

print("--------------------------------")

# Greater than / less than examples
temperature = 32  # degrees Celsius
print("Temperature:", temperature)
print("Is it hotter than 30 degrees?", temperature > 30)
print("Is it 30 degrees or colder?", temperature <= 30)

print("--------------------------------")

# Real-world style example: check if a cart total qualifies for free delivery
cart_total = 45
free_delivery_limit = 50

print("Cart total:", cart_total)
print("Free delivery limit:", free_delivery_limit)
print("Does the cart get free delivery?", cart_total >= free_delivery_limit)


