"""
07 - String Exercises
=====================
Practice problems to master string manipulation in Python.
"""

# ===================
# Exercise 1: Name Formatting
# ===================

print("=" * 50)
print("EXERCISE 1: Name Formatting")
print("=" * 50)

# TODO: Ask user for their name and print it in:
# - All uppercase
# - All lowercase
# - Title case

# Your solution here:
# name = input("Enter your name: ")
# print(f"Uppercase: {name.upper()}")
# print(f"Lowercase: {name.lower()}")
# print(f"Title Case: {name.title()}")

# Example with hardcoded value:
name = "john doe"
print(f"Original: {name}")
print(f"Uppercase: {name.upper()}")
print(f"Lowercase: {name.lower()}")
print(f"Title Case: {name.title()}")
print()

# ===================
# Exercise 2: Password Checker
# ===================

print("=" * 50)
print("EXERCISE 2: Password Checker")
print("=" * 50)

# TODO: Check if password is valid:
# - At least 8 characters long
# - Contains "@" symbol
# - Contains at least one digit

# Your solution here:
def check_password(password):
    """Check if password meets requirements"""
    is_long_enough = len(password) >= 8
    has_at_symbol = "@" in password
    has_digit = any(char.isdigit() for char in password)
    
    if is_long_enough and has_at_symbol and has_digit:
        return "Password is valid! ✓"
    else:
        errors = []
        if not is_long_enough:
            errors.append("- Must be at least 8 characters")
        if not has_at_symbol:
            errors.append("- Must contain @ symbol")
        if not has_digit:
            errors.append("- Must contain at least one digit")
        return "Password is invalid:\n" + "\n".join(errors)

# Test cases
print(check_password("Pass@123"))   # Valid
print(check_password("Short1"))     # Too short
print(check_password("NoAtSymbol1")) # No @
print(check_password("NoDigit@"))   # No digit
print()

# ===================
# Exercise 3: Word Counter
# ===================

print("=" * 50)
print("EXERCISE 3: Word Counter")
print("=" * 50)

# TODO: Count number of words in a sentence

# Your solution here:
sentence = "Python is an amazing programming language"
words = sentence.split()
word_count = len(words)
print(f"Sentence: {sentence}")
print(f"Word count: {word_count}")
print()

# ===================
# Exercise 4: Email Validator
# ===================

print("=" * 50)
print("EXERCISE 4: Email Validator")
print("=" * 50)

# TODO: Check if email is valid:
# - Contains exactly one @
# - Has text before and after @
# - Ends with .com, .org, or .edu

# Your solution here:
def validate_email(email):
    """Validate email format"""
    # Check @ count
    if email.count("@") != 1:
        return False
    
    # Split by @
    parts = email.split("@")
    username = parts[0]
    domain = parts[1]
    
    # Check username and domain
    if len(username) == 0 or len(domain) == 0:
        return False
    
    # Check domain extension
    valid_extensions = [".com", ".org", ".edu"]
    if not any(domain.endswith(ext) for ext in valid_extensions):
        return False
    
    return True

# Test cases
emails = [
    "user@example.com",    # Valid
    "invalid.email",       # No @
    "@example.com",        # No username
    "user@",               # No domain
    "user@example.net",    # Wrong extension
]

for email in emails:
    result = "Valid" if validate_email(email) else "Invalid"
    print(f"{email:25} -> {result}")
print()

# ===================
# Exercise 5: Palindrome Checker
# ===================

print("=" * 50)
print("EXERCISE 5: Palindrome Checker")
print("=" * 50)

# TODO: Check if a word is a palindrome (reads same forwards and backwards)

# Your solution here:
def is_palindrome(text):
    """Check if text is a palindrome"""
    # Remove spaces and convert to lowercase
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

# Test cases
words = ["radar", "python", "racecar", "A man a plan a canal Panama"]
for word in words:
    result = "Yes" if is_palindrome(word) else "No"
    print(f"'{word}' is palindrome? {result}")
print()

# ===================
# Exercise 6: Initials Generator
# ===================

print("=" * 50)
print("EXERCISE 6: Initials Generator")
print("=" * 50)

# TODO: Generate initials from full name

# Your solution here:
def get_initials(full_name):
    """Get initials from full name"""
    words = full_name.split()
    initials = "".join(word[0].upper() for word in words)
    return initials

# Test cases
names = [
    "John Doe",
    "Alice Bob Charlie",
    "Martin Luther King Jr"
]

for name in names:
    initials = get_initials(name)
    print(f"{name:30} -> {initials}")
print()

# ===================
# Exercise 7: Vowel Counter
# ===================

print("=" * 50)
print("EXERCISE 7: Vowel Counter")
print("=" * 50)

# TODO: Count number of vowels in a string

# Your solution here:
def count_vowels(text):
    """Count vowels in text"""
    vowels = "aeiouAEIOU"
    count = sum(1 for char in text if char in vowels)
    return count

# Test cases
sentences = [
    "Hello World",
    "Python Programming",
    "AEIOU",
    "xyz"
]

for sentence in sentences:
    count = count_vowels(sentence)
    print(f"'{sentence}' has {count} vowels")
print()

# ===================
# Exercise 8: Caesar Cipher
# ===================

print("=" * 50)
print("EXERCISE 8: Caesar Cipher")
print("=" * 50)

# TODO: Implement Caesar cipher (shift each letter by n positions)

# Your solution here:
def caesar_cipher(text, shift):
    """Encrypt text using Caesar cipher"""
    result = ""
    for char in text:
        if char.isalpha():
            # Determine if uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')
            # Shift character
            shifted = chr((ord(char) - start + shift) % 26 + start)
            result += shifted
        else:
            # Keep non-alphabetic characters as is
            result += char
    return result

# Test cases
message = "Hello World"
encrypted = caesar_cipher(message, 3)
decrypted = caesar_cipher(encrypted, -3)

print(f"Original:  {message}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
print()

# ===================
# Exercise 9: Word Reverser
# ===================

print("=" * 50)
print("EXERCISE 9: Word Reverser")
print("=" * 50)

# TODO: Reverse each word in a sentence but keep word order

# Your solution here:
def reverse_words(sentence):
    """Reverse each word in sentence"""
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)

# Test cases
sentence = "Hello World Python"
reversed_sentence = reverse_words(sentence)
print(f"Original:  {sentence}")
print(f"Reversed:  {reversed_sentence}")
print()

# ===================
# Exercise 10: Remove Duplicates
# ===================

print("=" * 50)
print("EXERCISE 10: Remove Duplicate Characters")
print("=" * 50)

# TODO: Remove duplicate characters while preserving order

# Your solution here:
def remove_duplicates(text):
    """Remove duplicate characters"""
    result = ""
    for char in text:
        if char not in result:
            result += char
    return result

# Test cases
words = ["hello", "programming", "mississippi"]
for word in words:
    cleaned = remove_duplicates(word)
    print(f"'{word}' -> '{cleaned}'")
print()

# ===================
# Exercise 11: Title Slug Generator
# ===================

print("=" * 50)
print("EXERCISE 11: Title Slug Generator")
print("=" * 50)

# TODO: Convert title to URL-friendly slug

# Your solution here:
def create_slug(title):
    """Create URL-friendly slug from title"""
    # Convert to lowercase
    slug = title.lower()
    # Replace spaces with hyphens
    slug = slug.replace(" ", "-")
    # Remove non-alphanumeric characters (except hyphens)
    slug = "".join(char for char in slug if char.isalnum() or char == "-")
    # Remove multiple consecutive hyphens
    while "--" in slug:
        slug = slug.replace("--", "-")
    # Remove leading/trailing hyphens
    slug = slug.strip("-")
    return slug

# Test cases
titles = [
    "Python Programming Tips",
    "Hello, World! 2024",
    "Advanced Python: Tips & Tricks"
]

for title in titles:
    slug = create_slug(title)
    print(f"{title:40} -> {slug}")
print()

# ===================
# Exercise 12: Anagram Checker
# ===================

print("=" * 50)
print("EXERCISE 12: Anagram Checker")
print("=" * 50)

# TODO: Check if two words are anagrams

# Your solution here:
def are_anagrams(word1, word2):
    """Check if two words are anagrams"""
    # Remove spaces and convert to lowercase
    clean1 = word1.replace(" ", "").lower()
    clean2 = word2.replace(" ", "").lower()
    # Sort characters and compare
    return sorted(clean1) == sorted(clean2)

# Test cases
word_pairs = [
    ("listen", "silent"),
    ("python", "typhon"),
    ("hello", "world"),
    ("The Eyes", "They See")
]

for word1, word2 in word_pairs:
    result = "Yes" if are_anagrams(word1, word2) else "No"
    print(f"'{word1}' and '{word2}' are anagrams? {result}")
print()

# ===================
# Bonus: Interactive Exercises
# ===================

print("=" * 50)
print("BONUS: Interactive Version")
print("=" * 50)
print("Uncomment the code below to make exercises interactive!")
print()

# Uncomment to make interactive:
"""
# Interactive Exercise 1: Name formatter
name = input("Enter your name: ")
print(f"Uppercase: {name.upper()}")
print(f"Lowercase: {name.lower()}")
print(f"Title Case: {name.title()}")

# Interactive Exercise 2: Password checker
password = input("Enter a password: ")
print(check_password(password))

# Interactive Exercise 3: Word counter
sentence = input("Enter a sentence: ")
words = sentence.split()
print(f"Word count: {len(words)}")

# Interactive Exercise 4: Palindrome checker
word = input("Enter a word: ")
if is_palindrome(word):
    print(f"'{word}' is a palindrome!")
else:
    print(f"'{word}' is not a palindrome.")
"""

print("\n" + "=" * 50)
print("All exercises completed! Great job! 🎉")
print("=" * 50)

