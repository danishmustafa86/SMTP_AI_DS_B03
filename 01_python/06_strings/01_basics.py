"""
01 - String Basics
==================
Learn how to create and work with strings in Python.
"""

# ===================
# Creating Strings
# ===================

# Single quotes
greeting = 'Hello'
print(greeting)  # Output: Hello

# Double quotes (exactly the same as single quotes)
message = "Welcome to Python"
print(message)  # Output: Welcome to Python

# Triple quotes for multi-line strings
long_text = """This is a 
multi-line string.
It can span several lines."""
print(long_text)

# Triple single quotes also work
another_long = '''Another way
to write
multi-line strings.'''
print(another_long)

# ===================
# When to use which quotes?
# ===================

# Use single quotes when your string contains double quotes
sentence1 = 'He said, "Hello!"'
print(sentence1)  # Output: He said, "Hello!"

# Use double quotes when your string contains single quotes
sentence2 = "It's a beautiful day"
print(sentence2)  # Output: It's a beautiful day

# Or use escape character (\) to include the same quote type
sentence3 = 'It\'s a beautiful day'
print(sentence3)  # Output: It's a beautiful day

sentence4 = "He said, \"Hello!\""
print(sentence4)  # Output: He said, "Hello!"

# ===================
# Empty Strings
# ===================

empty1 = ''
empty2 = ""
print(f"Empty string: '{empty1}'")  # Output: Empty string: ''
print(f"Length: {len(empty1)}")     # Output: Length: 0

# ===================
# String Type
# ===================

text = "Python"
print(type(text))  # Output: <class 'str'>

# Converting other types to strings
number = 42
text_number = str(number)
print(text_number)      # Output: 42
print(type(text_number))  # Output: <class 'str'>

pi = 3.14159
text_pi = str(pi)
print(text_pi)  # Output: 3.14159

# ===================
# String Length
# ===================

name = "Alice"
print(f"Length of '{name}': {len(name)}")  # Output: Length of 'Alice': 5

# Spaces count too!
phrase = "Hello World"
print(f"Length of '{phrase}': {len(phrase)}")  # Output: Length of 'Hello World': 11

# ===================
# Practice Examples
# ===================

# Example 1: Personal greeting
first_name = "John"
last_name = "Doe"
print("First name:", first_name)
print("Last name:", last_name)
print("Total characters:", len(first_name) + len(last_name))

# Example 2: Book title
book_title = 'The "Great" Adventure'
print("Book:", book_title)

# Example 3: Multi-line poem
poem = """Roses are red,
Violets are blue,
Python is awesome,
And so are you!"""
print(poem)

