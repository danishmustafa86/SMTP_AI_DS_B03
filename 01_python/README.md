## Module 1: Python


## Overall Goals

By the end of this module, you will be able to:

- **Write** small Python programs using variables, control flow, functions, and data structures on your own.
- **Work with data** such as strings, lists, dictionaries, files, and handle simple errors confidently.
- **Solve basic algorithmic problems** (for example, from LeetCode Easy) step by step.
- **Read and understand** simple Python code written by other people and explain what it does in your own words.
- **Use basic tooling**: run scripts, use an editor/IDE, and read error messages without feeling lost.

---

## Introduction & First Steps

**Main goals**
- Feel comfortable with the Python environment we will be using (editor, terminal, and how to run code).
- Successfully run your **first Python programs** by yourself.

**Topics**
- What Python is and where it is used (web, data, AI, automation), so you see why it is worth your time.
- How to install Python (if needed) and set up **VS Code**/**Cursor** or another editor.
- How to run Python code:
  - Run `python` / `python3` in the terminal.
  - Run simple `.py` files from your editor or terminal.
- **Real‑world example**
  - Imagine a simple chatbot or calculator app on your phone, and see how a small Python script can act like the “brain” behind that app.

**In‑class mini‑exercises**
- Locate Python on your machine and run a simple command in the terminal.
- Create a tiny `.py` file and run it, so you see the full flow from writing code to seeing output.

**Homework (light, non‑LeetCode yet)**
- Write 3–4 very small scripts to get comfortable:
  - Greet a user by name.
  - Convert Celsius to Fahrenheit.
  - Compute the perimeter of a rectangle.

---

## Variables, Input & Basic Errors

**Main goals**
- Understand **variables** and **user input** and use them comfortably.
- Read basic error messages without getting scared and to fix simple mistakes.

**Topics**
- Quick revision of Python basics with small examples:
  - Use `print()` and comments (`#`) to show output and document code.
  - Basic data types: integers, floats, strings, and booleans.
  - Simple arithmetic: `+ - * / // %` in small programs.
- Variables and assignment like `x = 5`, with naming rules and good style.
- `input()` with conversion using `int()` and `float()`.
- String concatenation vs `f-strings` for clearer messages.
- Basic errors:
  - Syntax errors (for example, missing `)` or `:`) and how Python reports them.
  - Runtime errors (for example, dividing by zero) and how to avoid them.
- Use `type()` to see the type of a variable and understand what data you are working with.
- **Real‑world examples**
  - Online form where a user enters name and age → map each field to variables and `input()`.
  - Small billing or grocery app where you enter prices and quantities → use variables and arithmetic to calculate totals.

**Code example – variables and arithmetic**

```python
# Arithmetic examples
x = 10
y = 3

print(x + y)   # 13
print(x * y)   # 30
print(x / y)   # 3.333...
print(x // y)  # 3  # integer division
print(x % y)   # 1  # remainder
```

**Code example – simple variables**

```python
# 'message' is the variable name, "Hello!" is the string value
message = "Hello!"
print(message)

# 'user_age' is the variable name, 25 is the integer value
user_age = 25
print(user_age)

# Update the variable
user_age = 26
print(user_age)
```

**In‑class mini‑exercises**
- Write a program that asks for name and age and then prints a message like: `"Hello Ali, you are 20 years old"`.
- Write a simple calculator where the user inputs two numbers and an operator (`+` or `-`) and the program prints the result.

**Practice**
- **Goal**: Feel comfortable with input, variables, and basic math in Python.

- **Suggested LeetCode Easy problems**
  - [1480. Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/) (if arrays are too early, think through it conceptually).
  - [1672. Richest Customer Wealth](https://leetcode.com/problems/richest-customer-wealth/) (also simple addition).
- **Custom practice problems**
  - Get length and width from user and print the area (length * width) and perimeter ( 2 * [length + width]) of a rectangle.
  - Ask the user for two numbers and print which one is larger or if they are equal.
  - Ask for a number of minutes and convert it to hours and minutes (for example, `130` minutes → `2 hours 10 minutes`).

---

## Conditions (if/elif/else) 
**Main goals**
- How to use `if`, `elif`, `else` to make decisions in your programs.

**Topics**
- Boolean expressions: `>`, `<`, `>=`, `<=`, `==`, `!=` to compare values.
- Syntax of `if`, `elif`, `else` (colon and indentation) and how Python follows these blocks.
- Combining conditions with `and`, `or`, `not` to express more complex logic.
- Simple nested `if` statements to see how decisions can be inside other decisions.
- **Real‑world examples**
  - Grading system that decides pass/fail or grade categories based on marks.
  - Simple login screen that checks username and password before allowing access.

**Code example – basic `if/elif/else`**

```python
score = 72

if score >= 80:
    grade = "A"
elif score >= 60:
    grade = "B"
else:
    grade = "C"

print("Your grade is:", grade)
```

**In‑class mini‑exercises**
- Program that checks if a number is positive, negative, or zero.
- Grading system where you input a score (0–100) and print grade `A/B/C/D/F`.
- Simple login check with a hard‑coded username and password.

---

## More Conditions & Simple Programs 
**Main goals**
- Practice conditions with small, real‑looking programs so you can apply `if`/`elif`/`else` confidently.

**Topics**
- Chained conditions with multiple `elif` to handle many cases cleanly.
- Simple menu programs using `if`/`elif` (for example, choosing options 1, 2, 3 in a console menu).
- **Logical thinking** with conditions (possibly using simple flow charts to visualize the decisions).

**Code example – simple menu with `if/elif`**

```python
print("1. Add")
print("2. Subtract")

choice = input("Choose 1 or 2: ")

if choice == "1":
    print("You chose Add")
elif choice == "2":
    print("You chose Subtract")
else:
    print("Invalid choice")
```

**In‑class mini‑exercises**
- Even‑or‑odd number checker.
- BMI calculator (enter height and weight, categorize as underweight/normal/overweight etc.).
- Basic calculator using `if`/`elif` for `+ - * /`.

**Practice (after you finish the conditions sections above)**
- **Goal**: Feel confident with conditions and comparisons.

- **Suggested LeetCode Easy problems**
  - [9. Palindrome Number](https://leetcode.com/problems/palindrome-number/) (only numeric version).
  - [412. Fizz Buzz](https://leetcode.com/problems/fizz-buzz/) (great for conditions and loops; I may revisit this later when we learn loops).
- **Custom practice problems**
  - Write a program that checks if a year is a leap year.
  - Write a program that decides if a student passes or fails based on multiple subject marks and overall average.
  - Write a simple traffic light helper: input color (`red`, `yellow`, `green`) and print what the driver should do.

---

## Loops – `while` 
**Main goals**
- Understand **repetition** with `while` loops.
- Begin thinking in loops instead of repeating code manually.

**Topics**
- Why loops are needed when similar tasks repeat again and again.
- `while` loop syntax and how the condition is checked each time.
- Loop variables and how to update them correctly inside the loop.
- What infinite loops look like and how to avoid them safely.
- **Real‑world examples**
  - Checking new messages in WhatsApp until there are none left → like a `while` loop.
  - Withdrawing money from an ATM until the balance is below a certain amount → loop condition.

**Code example – simple `while` loop**

```python
n = 1

while n <= 5:
    print(n)
    n += 1
```

**In‑class mini‑exercises**
- Print numbers 1 to 10 using a `while` loop.
- Sum numbers from 1 to `n` using a `while` loop.
- Guessing game where the program chooses a fixed number and you keep guessing until you are correct.

---

## Loops – `for`, `range`, and `break/continue`
**Main goals**
- Use `for` loops and `range` to repeat actions a specific number of times or over a collection.
- Control loops with `break` and `continue` so you can stop early or skip certain steps.

**Topics**
- `for` loop over `range(start, stop, step)`.
- Looping over characters in a string to process text one character at a time.
- Using `break` to stop a loop early.
- Using `continue` to skip the current iteration and move to the next one.
- **Real‑world examples**
  - Checking every message in a chat one by one → like looping over a list.
  - Scanning a list of students to find who passed → `for` loop with `if` conditions.

**Code example – `for` with `range` and `continue`**

```python
for n in range(1, 11):
    if n % 2 == 0:
        continue  # skip even numbers
    print(n)
```

**In‑class mini‑exercises**
- Print the multiplication table for a number (for example, 5).
- Count how many vowels are in a string using a loop.
- Print all numbers from 1 to 100 except multiples of 3 by using `continue`.

**Practice (after you finish the loop sections above)**
- **Goal**: Feel comfortable with both `for` and `while` loops.

- **Suggested LeetCode Easy problems**
  - [1342. Number of Steps to Reduce a Number to Zero](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/).
  - [383. Ransom Note](https://leetcode.com/problems/ransom-note/) (loop through characters; even if you don’t use dictionaries yet, you can still try it with basic tools).
- **Custom practice problems**
  - Print all even numbers between two given numbers.
  - Compute the factorial of a number using a loop.
  - Reverse a string using a loop (no slicing yet, unless I decide to show it as a shortcut).

---

## Functions – Basics
**Main goals**
- Want you to be able to define and use your own **functions**.
- Want you to understand parameters and return values and how data moves in and out of a function.

**Topics**
- Why we use functions: reuse, clarity, and better organization of code.
- Syntax: `def name(parameters):` and `return`.
- Local variables vs global variables (in a simple way, not too deep yet).
- Optionally, calling functions from a main block (`if __name__ == "__main__":`).
- **Real‑world examples**
  - Functions as small machines in a factory: input goes in, work happens, output comes out.
  - Calculator where each button (add, subtract, multiply) is like a separate function you can call.

**Code example – simple function**

```python
def add(a, b):
    return a + b

result = add(3, 5)
print("Sum:", result)
```

**In‑class mini‑exercises**
- Write a function that adds two numbers and returns the result.
- Write a function that checks if a number is prime (simple implementation).
- Write a function that computes the average of 3 numbers.

---

## More Functions & Problem Decomposition 
**Main goals**
- Break a bigger problem into multiple smaller functions.
- I want you to practice passing values into functions and returning results from them.

**Topics**
- Working with multiple parameters in a function.
- Using default parameter values when they make a function easier to use.
- Functions calling other functions to share work.
- Writing small utility functions and reusing them across different parts of a program.
- **Real‑world examples**
  - Planning an event where tasks are split (booking venue, sending invites, arranging food) → splitting a program into functions.
  - Using helper functions to clean and format data before saving it, like mini-tools inside a bigger app.

**Code example – function calling another function**

```python
def square(x):
    return x * x

def sum_of_squares(a, b):
    return square(a) + square(b)

print(sum_of_squares(2, 3))  # 13
```

**In‑class mini‑exercises**
- Build a calculator that uses separate functions for each operation.
- Write a function that counts vowels in a string.
- Write a function that takes a list of numbers and returns the max/min (preview of lists here).

**Practice (after you finish the function sections above)**
- **Goal**: Feel comfortable writing and using your own functions.

- **Suggested LeetCode Easy problems**
  - [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) (great for making helper functions).
  - [58. Length of Last Word](https://leetcode.com/problems/length-of-last-word/).
- **Custom practice problems**
  - Write a function to check if a number is perfect (sum of proper divisors = number).
  - Write a function that returns the greatest common divisor (GCD) of two numbers.
  - Write a function that takes a string and returns it in title case (first letter of each word capitalized).

---

## Lists – Basics 
**Main goals**
- How to use **lists** to store and work with collections of values.

**Topics**
- Create lists like `[]` and `[1, 2, 3]`.
- Access elements by index (including negative indices to count from the end).
- Basic list operations:
  - Use `append`, `insert`, `pop`, `remove`.
  - Use `len()` to check how many items are in a list.
- Iterate over lists with `for` loops.
- **Real‑world examples**
  - Shopping list on a phone → Python list of items.
  - List of student marks in a system → loop to compute averages.

**Code example – basic list operations**

```python
students = ["Ali", "Sara", "Omar"]
print(students[0])      # first student

students.append("Fatima")
print(len(students))    # 4

for name in students:
    print(name)
```

**In‑class mini‑exercises**
- Store 5 student names in a list and print them one per line.
- Take a list of numbers and compute the sum and average.
- Remove all occurrences of a given value from a list.

---

## More Lists & Basic List Algorithms 
**Main goals**
- Practice solving small problems using lists.

**Topics**
- Slicing: `list[start:end:step]`.
- Searching for an element in a list.
- Finding max and min manually (without `max()`/`min()` at first) to understand the logic.
- Brief intro to list comprehensions as a compact way to create lists.
- **Real‑world examples**
  - Cleaning up a contact list (removing duplicates, keeping only active contacts) → list operations.
  - Separating even and odd roll numbers in a class → splitting a list.

**Code example – splitting a list into even and odd**

```python
numbers = [1, 2, 3, 4, 5, 6]
evens = []
odds = []

for n in numbers:
    if n % 2 == 0:
        evens.append(n)
    else:
        odds.append(n)

print("Evens:", evens)
print("Odds:", odds)
```

**In‑class mini‑exercises**
- Find the second largest number in a list.
- Remove duplicates from a list using another list.
- Split a list into two lists: even numbers and odd numbers.

**Practice (after you finish the list sections above)**
- **Goal**: Feel confident manipulating lists and looping over them.

- **Suggested LeetCode Easy problems**
  - [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/).
  - [136. Single Number](https://leetcode.com/problems/single-number/).
- **Custom practice problems**
  - Merge two sorted lists into one sorted list.
  - Rotate a list to the right by `k` steps (simple version).
  - Take a list of numbers and move all zeros to the end (keeping the order of the other numbers the same).

---

## Strings in Detail

**Main goals**
- How to work comfortably with **strings**.

**Topics**
- Indexing and slicing strings.
- Common string methods: `lower()`, `upper()`, `strip()`, `split()`, `join()`, `replace()`.
- Checking membership using `in` / `not in`.
- Formatting strings nicely using `f-strings`.
- **Real‑world examples**
  - Cleaning and formatting user names and email addresses → string methods.
  - Processing a sentence from a chat or email → splitting and joining strings.

**Code example – cleaning and formatting text**

```python
text = "  hello, world!  "
clean = text.strip().upper()
print(clean)  # HELLO, WORLD!

words = clean.split(", ")
print(words)  # ['HELLO', 'WORLD!']
```

**In‑class mini‑exercises**
- Count how many times a character appears in a string.
- Reverse the words in a sentence.
- Check if a sentence is a palindrome (ignoring spaces and case).

---

## Dictionaries & Sets (Intro)
**Main goals**
- To understand **dictionaries** and **sets** conceptually and practically.

**Topics**
- Dictionaries:
  - Key–value pairs like `{"name": "Ali", "age": 20}`.
  - Accessing, adding, updating, and deleting entries.
  - Iterating over keys, values, and items.
- Sets:
  - Creating sets using `{1, 2, 3}` and `set()`.
  - No duplicates and fast membership tests.
  - Basic operations like union and intersection.
- **Real‑world examples**
  - Mini phonebook (name → phone number) → dictionary.
  - Removing duplicate email addresses from a mailing list → set.

**Code example – dictionary and set**

```python
student = {"name": "Ali", "age": 20}
print(student["name"])          # Ali

emails = {"a@example.com", "b@example.com", "a@example.com"}
print(emails)  # duplicate 'a@example.com' appears only once
```

**In‑class mini‑exercises**
- Store student info in a dictionary and print a nicely formatted output.
- Count word frequencies in a sentence (very basic word count).
- Take two lists and find common elements using sets.

**Practice (after you finish the strings and dictionary/set sections above)**
- **Goal**: Feel comfortable using strings, dictionaries, and sets for basic problems.

- **Suggested LeetCode Easy problems**
  - [387. First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/).
  - [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/).
- **Custom practice problems**
  - Take a sentence and output the top 3 most frequent words.
  - Replace all repeated characters in a string with `*` except the first occurrence.
  - Build a mini phonebook using a dictionary (name → phone) and allow simple lookup by name.

---

## Files & Basic Error Handling
**Main goals**
- To be able to read from and write to text files.
- To handle simple errors with `try/except` instead of letting your program crash.

**Topics**
- Opening files using `with open(...) as f:`.
- Reading file content using `read()`, `readline()`, and `readlines()`.
- Writing to files using modes like `"w"` and `"a"`.
- Exceptions using `try`, `except`, and optionally `finally`.
- **Real‑world examples**
  - Saving notes to a file like a mini notepad app.
  - Reading a configuration file or a simple log file for an application.

**Code example – write and read a file**

```python
# Write to a file
with open("notes.txt", "w") as f:
    f.write("Hello file!\n")

# Read from the same file
with open("notes.txt") as f:
    for line in f:
        print(line.strip())
```

**In‑class mini‑exercises**
- Read a text file and print each line with line numbers.
- Write user input to a file (simple note‑taking program).
- Safely read a file that may not exist and handle `FileNotFoundError` gracefully.

---

## Putting It Together – Small Project 
**Main goals**
- Combine **functions, loops, lists, strings, files** in a small but complete program.

**Topics**
- Plan a small project, for example: **To‑Do List app**, **Student grade manager**, or **Simple contact manager**.
- Break the project into functions and (optionally) modules.
- Use basic saving and loading of data from files so the project can remember information.

**In‑class activity**
- Build a small project step‑by‑step, for example:
  - **To‑Do app**  
    - Add a task.  
    - List tasks.  
    - Mark a task as done.  
    - Save tasks to a file.

**Practice (after you finish the files and project sections above)**
- **Goal**: Apply all your core Python knowledge in a slightly larger program.

- **Suggested LeetCode Easy problems**
  - [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/).
  - [929. Unique Email Addresses](https://leetcode.com/problems/unique-email-addresses/).
- **Custom practice problems**
  - Extend the class project (for example, add search, sorting, or simple filtering).
  - Write a program that reads a file and prints:
    - Number of lines
    - Number of words
    - Number of characters

---

## Intro to Modules & Standard Library 
**Main goals**
- To understand what modules are and how to use Python’s standard library.

**Topics**
- What a module is and how to `import` it, for example:
  - `import math`
  - `from random import randint`
- Basic modules:
  - `math` (functions like sqrt, ceil, floor).
  - `random` (functions like randint, choice).
  - `datetime` (working with current date and time).
- Brief intro to organizing code across multiple files.
- **Real‑world examples**
  - Generating OTP codes or random passwords → `random` module.
  - Showing the current date and time in an app → `datetime` module.

**Code example – using `random` and `datetime`**

```python
import random
from datetime import datetime

otp = random.randint(100000, 999999)
print("OTP:", otp)

now = datetime.now()
print("Current time:", now)
```

**In‑class mini‑exercises**
- Build simple random number games (guess the number).
- Generate a random password (letters/digits).
- Print the current date and time in a nice format.

---

## Review, Practice, and Next Steps 
**Main goals**
- Review all key concepts with you and practice problem‑solving together.
- To show you clear next steps after this module.

**Topics**
- Quick recap:
  - Variables, types, conditions, loops.
  - Functions.
  - Lists, strings, dictionaries, sets.
  - Files and error handling.
- Walk through 2–3 small end‑to‑end problems.
- Discuss next steps: OOP, more algorithms, data analysis, web development, etc.

**In‑class activity**
- Solve 2–3 LeetCode Easy problems live, step‑by‑step.
- Ask students to explain their ideas before coding.

**Final practice (after you finish all sections above)**
- **Suggested LeetCode Easy problems**
  - [1. Two Sum](https://leetcode.com/problems/two-sum/).
  - [13. Roman to Integer](https://leetcode.com/problems/roman-to-integer/).
- **Custom practice problems**
  - Design and implement a small project of your choice using what you have learned (you can prepare 2–3 suggested ideas as examples).

---



