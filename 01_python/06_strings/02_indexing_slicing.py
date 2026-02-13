"""
02 - String Indexing and Slicing
=================================
Learn how to access individual characters and parts of strings.
"""

# ===================
# String Indexing
# ===================

word = "Python"

# Positive indexing (starts from 0)
#  P  y  t  h  o  n
#  0  1  2  3  4  5

print("First character:", word[0])   # Output: P
print("Second character:", word[1])  # Output: y
print("Third character:", word[2])   # Output: t
print("Last character:", word[5])    # Output: n

# Negative indexing (starts from -1 at the end)
#  P  y  t  h  o  n
# -6 -5 -4 -3 -2 -1

print("Last character:", word[-1])    # Output: n
print("Second to last:", word[-2])    # Output: o
print("First character:", word[-6])   # Output: P

# ===================
# String Slicing
# ===================

# Syntax: string[start:end]
# - includes start index
# - excludes end index

text = "Hello World"

# Basic slicing
print(text[0:5])   # Output: Hello (characters 0,1,2,3,4)
print(text[6:11])  # Output: World (characters 6,7,8,9,10)

# Omitting start (starts from beginning)
print(text[:5])    # Output: Hello (same as [0:5])

# Omitting end (goes to the end)
print(text[6:])    # Output: World (from 6 to end)

# Both omitted (copies entire string)
print(text[:])     # Output: Hello World

# ===================
# Slicing with Step
# ===================

# Syntax: string[start:end:step]

alphabet = "ABCDEFGHIJ"

# Every second character
print(alphabet[::2])    # Output: ACEGI

# Every third character
print(alphabet[::3])    # Output: ADGJ

# Reverse a string (step of -1)
print(alphabet[::-1])   # Output: JIHGFEDCBA

# Reverse with start and end
print(alphabet[7:2:-1]) # Output: HGFED

# ===================
# Practical Examples
# ===================

# Example 1: Email parsing
email = "john.doe@example.com"
username = email[:8]      # john.doe
domain = email[9:]        # example.com
print(f"Username: {username}")
print(f"Domain: {domain}")

# Example 2: Get file extension
filename = "document.pdf"
extension = filename[-3:] # pdf
print(f"Extension: {extension}")

# Example 3: First and last name
full_name = "Alice Johnson"
space_index = full_name.find(" ")  # Find space position
first = full_name[:space_index]    # Alice
last = full_name[space_index+1:]   # Johnson
print(f"First: {first}, Last: {last}")

# Example 4: Extracting date parts
date = "2025-12-27"
year = date[:4]    # 2025
month = date[5:7]  # 12
day = date[8:]     # 27
print(f"Year: {year}, Month: {month}, Day: {day}")

# Example 5: Every other character
message = "HELLO"
print(message[::2])  # Output: HLO

# Example 6: Palindrome check
word1 = "radar"
word2 = "python"
print(f"'{word1}' reversed: {word1[::-1]}")  # radar
print(f"Is '{word1}' a palindrome? {word1 == word1[::-1]}")  # True
print(f"Is '{word2}' a palindrome? {word2 == word2[::-1]}")  # False

# ===================
# Common Mistakes
# ===================

sample = "Python"

# IndexError: trying to access index that doesn't exist
# print(sample[10])  # ERROR! Would raise IndexError

# But slicing doesn't raise errors - it just gives what's available
print(sample[10:20])  # Output: (empty string)
print(sample[2:100])  # Output: thon

# ===================
# Practice Challenges
# ===================

# Challenge 1: Get middle character
text = "Python"
middle_index = len(text) // 2
print(f"Middle character of '{text}': {text[middle_index]}")

# Challenge 2: Get first 3 and last 3 characters
word = "Programming"
first_three = word[:3]
last_three = word[-3:]
print(f"First 3: {first_three}, Last 3: {last_three}")

# Challenge 3: Remove first and last character
word = "Hello"
middle = word[1:-1]
print(f"Without first and last: {middle}")  # Output: ell

