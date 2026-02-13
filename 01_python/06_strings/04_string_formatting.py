"""
04 - String Formatting
======================
Learn different ways to format and combine strings with variables.
"""

# ===================
# Method 1: String Concatenation (Basic)
# ===================

name = "Alice"
age = 25

# Using + operator
message = "Hello, " + name + "!"
print(message)  # Output: Hello, Alice!

# Must convert non-strings
message = name + " is " + str(age) + " years old"
print(message)  # Output: Alice is 25 years old

# Using multiple print arguments
print("Hello,", name, "!")  # Output: Hello, Alice !

# ===================
# Method 2: %-formatting (Old Style)
# ===================

name = "Bob"
age = 30

# %s for strings, %d for integers, %f for floats
message = "Hello, %s! You are %d years old." % (name, age)
print(message)  # Output: Hello, Bob! You are 30 years old.

name = "Charlie"
age = 35

# Positional arguments
message = "Hello, {}! You are {} years old.".format(name, age)
print(message)  # Output: Hello, Charlie! You are 35 years old.

# Indexed arguments
message = "Hello, {0}! {0} is {1} years old.".format(name, age)
print(message)  # Output: Hello, Charlie! Charlie is 35 years old.

# Named arguments
message = "Hello, {name}! You are {age} years old.".format(name=name, age=age)
print(message)  # Output: Hello, Charlie! You are 35 years old.

# Number formatting
pi = 3.14159
print("Pi is approximately {:.2f}".format(pi))  # Output: Pi is approximately 3.14

price = 49.5
print("Price: ${:.2f}".format(price))  # Output: Price: $49.50

# ===================
# Method 4: f-strings (Modern & Recommended) ⭐
# ===================

name = "Diana"
age = 28

# Basic f-string
message = f"Hello, {name}! You are {age} years old."
print(message)  # Output: Hello, Diana! You are 28 years old.

# Expressions inside f-strings
print(f"{name} will be {age + 1} next year")

# Calling methods inside f-strings
text = "python"
print(f"Uppercase: {text.upper()}")  # Output: Uppercase: PYTHON

# Number formatting with f-strings
pi = 3.14159
print(f"Pi is approximately {pi:.2f}")  # Output: Pi is approximately 3.14

# Large numbers with thousand separators
population = 1234567890
print(f"Population: {population:,}")  # Output: Population: 1,234,567,890

# Percentage formatting
accuracy = 0.9567
print(f"Accuracy: {accuracy:.1%}")  # Output: Accuracy: 95.7%

# ===================
# Alignment and Padding with f-strings
# ===================

name = "Alice"

# Left align (default for strings)
print(f"|{name:<10}|")  # Output: |Alice     |

# Right align
print(f"|{name:>10}|")  # Output: |     Alice|

# Center align
print(f"|{name:^10}|")  # Output: |  Alice   |

# With custom fill character
print(f"|{name:*^10}|")  # Output: |**Alice***|

# Number alignment
number = 42
print(f"|{number:5}|")   # Output: |   42|
print(f"|{number:05}|")  # Output: |00042| (zero padding)

# ===================
# Multi-line f-strings
# ===================

name = "Bob"
age = 30
city = "New York"

# Multi-line string with f-string
info = f"""
Name: {name}
Age: {age}
City: {city}
Next year: {age + 1}
"""
print(info)

# ===================
# Practical Examples
# ===================

# Example 1: Receipt
item = "Laptop"
price = 999.99
quantity = 2
total = price * quantity

receipt = f"""
{'RECEIPT':^30}
{'='*30}
Item: {item}
Price: ${price:.2f}
Quantity: {quantity}
{'='*30}
Total: ${total:.2f}
"""
print(receipt)

# Example 2: Progress bar
completed = 45
total_tasks = 100
percentage = (completed / total_tasks) * 100

print(f"Progress: {completed}/{total_tasks} ({percentage:.1f}%)")
print(f"[{'='*int(percentage/2):.<50}]")

# Example 3: Table formatting
print(f"{'Name':<15} {'Age':>5} {'City':<15}")
print(f"{'-'*15} {'-'*5} {'-'*15}")
print(f"{'Alice':<15} {25:>5} {'New York':<15}")
print(f"{'Bob':<15} {30:>5} {'Los Angeles':<15}")
print(f"{'Charlie':<15} {35:>5} {'Chicago':<15}")

# Example 4: Time formatting
hours = 9
minutes = 5
seconds = 3
print(f"Time: {hours:02d}:{minutes:02d}:{seconds:02d}")  # Output: Time: 09:05:03

# Example 5: Scientific notation
big_number = 1234567890
print(f"Scientific: {big_number:e}")  # Output: Scientific: 1.234568e+09

# Example 6: Binary, Octal, Hex
number = 42
print(f"Decimal: {number}")
print(f"Binary: {number:b}")
print(f"Octal: {number:o}")
print(f"Hexadecimal: {number:x}")

# Example 7: Dynamic width
width = 20
name = "Python"
print(f"|{name:^{width}}|")  # Width can be a variable!

# Example 8: Debugging (Python 3.8+)
x = 10
y = 20
print(f"{x=}, {y=}, {x+y=}")  # Output: x=10, y=20, x+y=30

# ===================
# Best Practices
# ===================

# ✅ DO: Use f-strings for most cases (modern & readable)
name = "Alice"
age = 25
print(f"{name} is {age} years old")

# ✅ DO: Use .format() for template strings
template = "Hello, {name}! Welcome to {place}."
print(template.format(name="Bob", place="Python"))

# ❌ DON'T: Use concatenation for complex formatting
# Harder to read:
print(name + " is " + str(age) + " years old")

# ===================
# Common Format Specifiers
# ===================

value = 1234.5678

print(f"{value:.2f}")    # 2 decimal places: 1234.57
print(f"{value:10.2f}")  # Width 10, 2 decimals:    1234.57
print(f"{value:010.2f}") # Zero padding: 0001234.57
print(f"{value:,.2f}")   # Thousand separator: 1,234.57
print(f"{value:e}")      # Scientific: 1.234568e+03

