"""
05 - String Operations
=======================
Learn string concatenation, repetition, membership, and comparison.
"""

# ===================
# String Concatenation
# ===================

# Concatenation with + operator
first = "Hello"
second = "World"
result = first + " " + second
print(result)  # Output: Hello World

# Multiple concatenations
greeting = "Hello" + " " + "beautiful" + " " + "world"
print(greeting)  # Output: Hello beautiful world

# Concatenating with other strings
name = "Alice"
message = "Welcome, " + name + "!"
print(message)  # Output: Welcome, Alice!

# Building a path (but os.path.join is better for real use)
folder = "documents"
subfolder = "reports"
filename = "data.txt"
path = folder + "/" + subfolder + "/" + filename
print(path)  # Output: documents/reports/data.txt

# ===================
# String Repetition
# ===================

# Repetition with * operator
echo = "Ha" * 3
print(echo)  # Output: HaHaHa

# Creating separators
separator = "=" * 40
print(separator)  # Output: ========================================

# Creating patterns
pattern = "+-" * 10
print(pattern)  # Output: +-+-+-+-+-+-+-+-+-+-

# Empty string repeated is still empty
nothing = "" * 100
print(f"Length: {len(nothing)}")  # Output: Length: 0

# Practical: Creating borders
line = "*" * 50
title = "Welcome to Python"
print(line)
print(title.center(50))
print(line)

# ===================
# Membership Testing
# ===================

# Check if substring exists with 'in'
sentence = "Python is awesome"
print("Python" in sentence)     # Output: True
print("Java" in sentence)       # Output: False
print("awesome" in sentence)    # Output: True

# Check if substring does NOT exist with 'not in'
print("Ruby" not in sentence)   # Output: True
print("Python" not in sentence) # Output: False

# Case-sensitive!
print("python" in sentence)     # Output: False (lowercase)
print("PYTHON" in sentence)     # Output: False (uppercase)

# Case-insensitive check
print("python" in sentence.lower())  # Output: True

# Checking for multiple substrings
email = "user@example.com"
if "@" in email and "." in email:
    print("Valid email format")

# Practical examples
password = "MySecure123"
if "@" in password:
    print("Password contains @")
else:
    print("Password does NOT contain @")

text = "Learning Python is fun"
if "Python" in text:
    print("This text is about Python!")

# ===================
# String Comparison
# ===================

# Equality comparison
print("hello" == "hello")   # Output: True
print("hello" == "Hello")   # Output: False (case-sensitive)

# Inequality comparison
print("apple" != "orange")  # Output: True
print("test" != "test")     # Output: False

# Lexicographic comparison (alphabetical order)
print("apple" < "banana")   # Output: True (a comes before b)
print("cat" > "car")        # Output: True (t comes after r)
print("abc" <= "abc")       # Output: True (equal)

# Uppercase letters come before lowercase in ASCII
print("Apple" < "apple")    # Output: True (A=65, a=97 in ASCII)
print("Z" < "a")            # Output: True

# Comparing by length doesn't work directly
print("aaa" < "z")          # Output: True (compares alphabetically, not length)

# Length comparison (do it explicitly)
str1 = "hello"
str2 = "hi"
print(len(str1) > len(str2))  # Output: True

# ===================
# String Immutability
# ===================

# Strings cannot be changed in place!
text = "Hello"
# text[0] = "h"  # ERROR! TypeError: 'str' object does not support item assignment

# Instead, create a new string
text = "h" + text[1:]
print(text)  # Output: hello

# All string methods return NEW strings
original = "python"
uppercase = original.upper()
print(f"Original: {original}")   # Output: Original: python (unchanged)
print(f"Uppercase: {uppercase}") # Output: Uppercase: PYTHON

# This is why we reassign:
message = "  hello  "
message = message.strip()  # Create new string and assign back
print(f"'{message}'")  # Output: 'hello'

# ===================
# Iterating Over Strings
# ===================

# For loop through characters
word = "Python"
for char in word:
    print(char)
# Output:
# P
# y
# t
# h
# o
# n

# With index and character
for i, char in enumerate(word):
    print(f"Index {i}: {char}")

# Count specific character
text = "Hello World"
count_l = 0
for char in text:
    if char.lower() == 'l':
        count_l += 1
print(f"Number of 'l's: {count_l}")  # Output: Number of 'l's: 3

# ===================
# Practical Examples
# ===================

# Example 1: Build a menu
print("=" * 40)
print("MAIN MENU".center(40))
print("=" * 40)
print("1. Option One")
print("2. Option Two")
print("3. Option Three")
print("=" * 40)

# Example 2: Check file extension
filename = "document.pdf"
if filename.endswith(".pdf"):
    print("This is a PDF file")
elif filename.endswith((".jpg", ".png")):
    print("This is an image file")

# Example 3: Count vowels
text = "Hello World"
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count += 1
print(f"Number of vowels: {count}")  # Output: Number of vowels: 3

# Example 4: Create a simple password validator
password = "Pass123"
has_digit = any(char.isdigit() for char in password)
has_alpha = any(char.isalpha() for char in password)
long_enough = len(password) >= 6

if has_digit and has_alpha and long_enough:
    print("Password is valid")
else:
    print("Password is invalid")

# Example 5: Check if two strings are anagrams
word1 = "listen"
word2 = "silent"
is_anagram = sorted(word1) == sorted(word2)
print(f"'{word1}' and '{word2}' are anagrams: {is_anagram}")

# Example 6: Create initials
full_name = "John Fitzgerald Kennedy"
words = full_name.split()
initials = ""
for word in words:
    initials += word[0].upper()
print(f"Initials: {initials}")  # Output: Initials: JFK

# Example 7: Reverse words in sentence
sentence = "Hello World Python"
words = sentence.split()
reversed_words = " ".join(words[::-1])
print(f"Reversed: {reversed_words}")  # Output: Reversed: Python World Hello

# Example 8: Remove duplicate characters (preserve order)
text = "programming"
unique = ""
for char in text:
    if char not in unique:
        unique += char
print(f"Unique characters: {unique}")  # Output: Unique characters: progamin

# ===================
# Common Patterns
# ===================

# Pattern 1: Build string from parts
parts = ["Python", "is", "awesome"]
sentence = " ".join(parts)
print(sentence)

# Pattern 2: Check multiple conditions
text = "Hello123"
if text.isalnum() and len(text) > 5:
    print("Valid username")

# Pattern 3: First character uppercase, rest lowercase
name = "jOHN"
formatted = name[0].upper() + name[1:].lower()
print(formatted)  # Output: John

# Pattern 4: Swap two parts of a string
email = "user@example.com"
parts = email.split("@")
swapped = parts[1] + "@" + parts[0]
print(swapped)  # Output: example.com@user

