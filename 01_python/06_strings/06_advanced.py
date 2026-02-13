"""
06 - Advanced String Concepts
==============================
Learn escape characters, raw strings, Unicode, and more advanced topics.
"""

# ===================
# Escape Characters
# ===================

# \n - newline
print("Line 1\nLine 2\nLine 3")
# Output:
# Line 1
# Line 2
# Line 3

# \t - tab
print("Name:\tAlice\nAge:\t25")
# Output:
# Name:   Alice
# Age:    25

# \\ - backslash
path = "C:\\Users\\Documents\\file.txt"
print(path)  # Output: C:\Users\Documents\file.txt

# \' and \" - quotes
print('It\'s a nice day')    # Output: It's a nice day
print("He said, \"Hello!\"") # Output: He said, "Hello!"

# \r - carriage return (rarely used)
print("Hello\rWorld")  # Output: World (overwrites)

# \b - backspace (rarely used)
print("Hello\bWorld")  # Output: HellWorld

# Common escape sequences summary
escapes = """
Common Escape Sequences:
\\n  - newline
\\t  - tab
\\\\  - backslash
\\'  - single quote
\\"  - double quote
"""
print(escapes)

# ===================
# Raw Strings
# ===================

# Raw strings (prefix with r or R) treat backslashes as literal
# Useful for Windows paths and regular expressions

# Without raw string (need to escape backslashes)
path1 = "C:\\Users\\Documents\\file.txt"
print(path1)

# With raw string (no escaping needed)
path2 = r"C:\Users\Documents\file.txt"
print(path2)

# Useful for regular expressions
regex = r"\d{3}-\d{3}-\d{4}"  # Phone number pattern
print(regex)  # Output: \d{3}-\d{3}-\d{4}

# Without raw string, you'd need double backslashes
regex_escaped = "\\d{3}-\\d{3}-\\d{4}"
print(regex_escaped)  # Same output but harder to read

# Note: Raw strings still interpret quotes
print(r"Can't end with backslash: \\")  # Output: Can't end with backslash: \\

# ===================
# Unicode and Encoding
# ===================

# Python 3 strings are Unicode by default
text = "Hello 世界 🌍"
print(text)  # Output: Hello 世界 🌍

# Unicode escape sequences
heart = "\u2764"  # ❤
print(f"I {heart} Python")

# More Unicode examples
emoji = "\U0001F600"  # 😀
print(emoji)

# Check if character is in string
text = "Python 🐍"
print("🐍" in text)  # Output: True

# Length counts characters, not bytes
text = "Hello"
print(len(text))  # Output: 5

text_emoji = "Hello 🌍"
print(len(text_emoji))  # Output: 7 (emoji is 1 character)

# Encoding to bytes
text = "Hello"
bytes_data = text.encode('utf-8')
print(bytes_data)  # Output: b'Hello'
print(type(bytes_data))  # Output: <class 'bytes'>

# Decoding from bytes
decoded = bytes_data.decode('utf-8')
print(decoded)  # Output: Hello

# ===================
# String Module
# ===================

import string

# Pre-defined character sets
print("Lowercase:", string.ascii_lowercase)
# Output: abcdefghijklmnopqrstuvwxyz

print("Uppercase:", string.ascii_uppercase)
# Output: ABCDEFGHIJKLMNOPQRSTUVWXYZ

print("Digits:", string.digits)
# Output: 0123456789

print("Punctuation:", string.punctuation)
# Output: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

print("Whitespace:", repr(string.whitespace))
# Output: ' \t\n\r\x0b\x0c'

# Practical: Check if password contains special character
password = "Pass@123"
has_special = any(char in string.punctuation for char in password)
print(f"Has special character: {has_special}")  # Output: True

# Practical: Generate random password
import random
chars = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(chars) for _ in range(12))
print(f"Random password: {password}")

# ===================
# String Interning
# ===================

# Python optimizes memory by reusing immutable strings
a = "hello"
b = "hello"
print(a is b)  # Output: True (same object in memory)

# Works for short strings and identifiers
x = "python"
y = "python"
print(id(x) == id(y))  # Output: True

# May not work for long strings or strings with spaces
long1 = "a" * 1000
long2 = "a" * 1000
print(long1 is long2)  # May be False

# ===================
# String Methods - Advanced
# ===================

# partition() - split string into 3 parts
text = "user@example.com"
before, sep, after = text.partition("@")
print(f"Before: {before}, Sep: {sep}, After: {after}")
# Output: Before: user, Sep: @, After: example.com

# rpartition() - partition from right
path = "C:/Users/Documents/file.txt"
folder, sep, filename = path.rpartition("/")
print(f"Folder: {folder}, File: {filename}")
# Output: Folder: C:/Users/Documents, File: file.txt

# translate() - character mapping
# Remove all vowels
text = "Hello World"
vowels = "aeiouAEIOU"
translator = str.maketrans("", "", vowels)
result = text.translate(translator)
print(result)  # Output: Hll Wrld

# Replace characters with mapping
text = "Hello World"
mapping = str.maketrans("aeiou", "12345")
result = text.translate(mapping)
print(result)  # Output: H2ll4 W4rld

# expandtabs() - convert tabs to spaces
text = "Name:\tAlice\nAge:\t25"
print(text.expandtabs(4))  # 4 spaces per tab

# splitlines() - split by line breaks
text = "Line 1\nLine 2\nLine 3"
lines = text.splitlines()
print(lines)  # Output: ['Line 1', 'Line 2', 'Line 3']

# ===================
# Regular Expressions (Basics)
# ===================

import re

# Find all digits in string
text = "My phone number is 123-456-7890"
digits = re.findall(r'\d+', text)
print(digits)  # Output: ['123', '456', '7890']

# Check if string matches pattern
email = "user@example.com"
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
if re.match(pattern, email):
    print("Valid email format")

# Replace using regex
text = "My phone is 123-456-7890 and 987-654-3210"
hidden = re.sub(r'\d', '*', text)
print(hidden)  # Output: My phone is ***-***-**** and ***-***-****

# Split by multiple delimiters
text = "apple,banana;cherry:date"
fruits = re.split(r'[,;:]', text)
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'date']

# ===================
# Practical Advanced Examples
# ===================

# Example 1: Pretty print JSON-like string
data = '{"name": "Alice", "age": 25, "city": "NYC"}'
formatted = data.replace(",", ",\n  ").replace("{", "{\n  ").replace("}", "\n}")
print(formatted)

# Example 2: Mask credit card number
card = "1234-5678-9012-3456"
masked = card[:5] + "*" * 9 + card[-4:]
print(masked)  # Output: 1234-*********3456

# Example 3: Word wrap
text = "This is a very long sentence that needs to be wrapped to fit nicely."
words = text.split()
line = ""
for word in words:
    if len(line) + len(word) + 1 <= 30:
        line += word + " "
    else:
        print(line.strip())
        line = word + " "
print(line.strip())

# Example 4: Extract hashtags
tweet = "Learning #Python is fun! #coding #developer"
hashtags = [word for word in tweet.split() if word.startswith("#")]
print(hashtags)  # Output: ['#Python', '#coding', '#developer']

# Example 5: Title case for names (handle special cases)
def format_name(name):
    """Format name with proper capitalization"""
    # Handle names like McDonald, O'Brien
    special_cases = ["mc", "mac", "o'"]
    
    parts = name.lower().split()
    result = []
    for part in parts:
        if any(part.startswith(prefix) for prefix in special_cases):
            # Special handling
            if part.startswith("mc"):
                formatted = "Mc" + part[2:].capitalize()
            elif part.startswith("o'"):
                formatted = "O'" + part[2:].capitalize()
            else:
                formatted = part.capitalize()
        else:
            formatted = part.capitalize()
        result.append(formatted)
    return " ".join(result)

print(format_name("john mcdonald"))  # Output: John McDonald
print(format_name("patrick o'brien"))  # Output: Patrick O'Brien

# Example 6: Slugify (convert to URL-friendly string)
def slugify(text):
    """Convert text to URL-friendly slug"""
    # Lowercase, replace spaces with hyphens, remove special chars
    slug = text.lower()
    slug = slug.replace(" ", "-")
    slug = "".join(char for char in slug if char.isalnum() or char == "-")
    return slug

title = "Python Tips & Tricks 2024!"
print(slugify(title))  # Output: python-tips--tricks-2024

# Example 7: Truncate with ellipsis
def truncate(text, max_length=50):
    """Truncate text to max length with ellipsis"""
    if len(text) <= max_length:
        return text
    return text[:max_length-3] + "..."

long_text = "This is a very long text that needs to be truncated for display purposes."
print(truncate(long_text, 30))  # Output: This is a very long text...

