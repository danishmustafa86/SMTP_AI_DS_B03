# We join strings when we want to build messages, emails, and labels from smaller text pieces.
# Joining (concatenating) strings together.

first_name = "Danish"
last_name = "Mustafa"

a = 34
# Simple string concatenation with +
full_name = first_name + " " + last_name

# print("Full name (using +):", full_name)

# # Concatenation using f-strings (recommended)
age = 25
message = f"My name is {full_name} and I am {age} years old."
print("Using f-string:", message)

