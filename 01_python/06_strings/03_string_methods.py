"""
03 - String Methods
====================
Learn the most useful built-in string methods.
"""

# ===================
# Case Conversion Methods
# ===================

text = "Hello World"

# Convert to lowercase
print(text.lower())      # Output: hello world

# Convert to uppercase
print(text.upper())      # Output: HELLO WORLD

# Title case (first letter of each word capitalized)
print(text.title())      # Output: Hello World

# Capitalize (only first letter of entire string)
print(text.capitalize()) # Output: Hello world

# Swap case (upper ↔ lower)
print(text.swapcase())   # Output: hELLO wORLD

# Example: case-insensitive comparison
password = "SECRET"
user_input = "secret"
if password.lower() == user_input.lower():
    print("Password matches!")

# ===================
# Stripping Whitespace
# ===================

messy = "   Hello World   "

# Remove whitespace from both ends
print(f"'{messy.strip()}'")   # Output: 'Hello World'

# Remove whitespace from left only
print(f"'{messy.lstrip()}'")  # Output: 'Hello World   '

# Remove whitespace from right only
print(f"'{messy.rstrip()}'")  # Output: '   Hello World'

# Strip specific characters
url = "https://example.com/"
print(url.strip("/"))  # Output: https://example.com
print(url.rstrip("/")) # Output: https://example.com

# ===================
# Finding and Replacing
# ===================

sentence = "Python is fun. Python is powerful."

# Find position of substring (returns -1 if not found)
print(sentence.find("is"))        # Output: 7 (first occurrence)
print(sentence.find("Java"))      # Output: -1 (not found)

# Find with start position
print(sentence.find("Python", 1)) # Output: 15 (skip first one)

# Index (like find, but raises error if not found)
print(sentence.index("fun"))      # Output: 10

# Count occurrences
print(sentence.count("Python"))   # Output: 2
print(sentence.count("is"))       # Output: 2

# Replace substring
new_sentence = sentence.replace("Python", "Java")
print(new_sentence)  # Output: Java is fun. Java is powerful.

# Replace with limit
limited = sentence.replace("Python", "Java", 1)
print(limited)  # Output: Java is fun. Python is powerful.

# ===================
# Checking String Content
# ===================

# Check if string starts with substring
filename = "document.pdf"
print(filename.startswith("doc"))    # Output: True
print(filename.startswith("image"))  # Output: False

# Check if string ends with substring
print(filename.endswith(".pdf"))     # Output: True
print(filename.endswith(".jpg"))     # Output: False

# Check if string contains only letters
print("Hello".isalpha())      # Output: True
print("Hello123".isalpha())   # Output: False

# Check if string contains only digits
print("12345".isdigit())      # Output: True
print("123.45".isdigit())     # Output: False

# Check if string contains only alphanumeric
print("Hello123".isalnum())   # Output: True
print("Hello 123".isalnum())  # Output: False (space)

# Check if string is all lowercase
print("hello".islower())      # Output: True
print("Hello".islower())      # Output: False

# Check if string is all uppercase
print("HELLO".isupper())      # Output: True
print("Hello".isupper())      # Output: False

# Check if string is all whitespace
print("   ".isspace())        # Output: True
print("  a ".isspace())       # Output: False

# ===================
# Splitting and Joining
# ===================

# Split string into list
text = "apple,banana,cherry"
fruits = text.split(",")
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# Split by whitespace (default)
sentence = "The quick brown fox"
words = sentence.split()
print(words)  # Output: ['The', 'quick', 'brown', 'fox']

# Split with limit
text = "one,two,three,four"
parts = text.split(",", 2)
print(parts)  # Output: ['one', 'two', 'three,four']

# Join list into string
fruits = ["apple", "banana", "cherry"]
result = ", ".join(fruits)
print(result)  # Output: apple, banana, cherry

# Join with different separator
result2 = " | ".join(fruits)
print(result2)  # Output: apple | banana | cherry

# Join words
words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print(sentence)  # Output: Python is awesome

# ===================
# Alignment and Padding
# ===================

text = "Python"

# Center align (total width 20)
print(text.center(20))       # Output:        Python       
print(text.center(20, "*"))  # Output: *******Python*******

# Left align
print(text.ljust(20))        # Output: Python              
print(text.ljust(20, "-"))   # Output: Python--------------

# Right align
print(text.rjust(20))        # Output:               Python
print(text.rjust(20, "-"))   # Output: --------------Python

# Zero padding (useful for numbers)
num = "42"
print(num.zfill(5))          # Output: 00042

# ===================
# Practical Examples
# ===================

# Example 1: Clean user input
user_input = "  JoHn DoE  "
cleaned = user_input.strip().title()
print(f"Cleaned name: {cleaned}")  # Output: Cleaned name: John Doe

# Example 2: Email validation (basic)
email = "user@example.com"
if "@" in email and email.endswith(".com"):
    print("Email format looks valid")

# Example 3: Create a table
print("Name".ljust(15) + "Age".rjust(5))
print("Alice".ljust(15) + "25".rjust(5))
print("Bob".ljust(15) + "30".rjust(5))

# Example 4: Word counter
text = "Python is fun and Python is powerful"
words = text.lower().split()
python_count = words.count("python")
print(f"'Python' appears {python_count} times")

# Example 5: File extension checker
files = ["image.jpg", "document.pdf", "script.py", "data.csv"]
for file in files:
    if file.endswith((".jpg", ".png", ".gif")):
        print(f"{file} is an image")
    elif file.endswith(".pdf"):
        print(f"{file} is a PDF")
    elif file.endswith(".py"):
        print(f"{file} is a Python script")

# Example 6: Remove all spaces
text = "Hello World Python"
no_spaces = text.replace(" ", "")
print(no_spaces)  # Output: HelloWorldPython

# Example 7: Password strength checker
password = "Pass1234"
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)
is_long = len(password) >= 8

if has_upper and has_lower and has_digit and is_long:
    print("Strong password!")
else:
    print("Weak password")

