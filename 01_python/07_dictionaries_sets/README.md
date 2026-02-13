# 07 – Dictionaries and Sets

This folder introduces **dictionaries** and **sets**, two powerful collection types.

## Dictionaries (key–value pairs)

- **Creating a dictionary**  
  `student = {"name": "Ali", "age": 20}`

- **Accessing and updating values**  
  Use keys: `student["name"]`, `student["age"] = 21`.

- **Common methods**  
  `keys()`, `values()`, `items()`, `get()`, `pop()`, `update()`.

## Sets (unique unordered items)

- **Creating a set**  
  `numbers = {1, 2, 3, 3}` results in `{1, 2, 3}` (no duplicates).

- **Set operations**  
  Union (`|`), intersection (`&`), difference (`-`) to compare sets.

## Why this matters

Use dictionaries to model real-world objects with named fields, and sets when you need **unique items** and **fast membership checks**.

## Practice exercises

1. **Student info**  
   Create a dictionary for a student with keys like `"name"`, `"age"`, and `"grade"`, then print a formatted description.

2. **Word frequency**  
   Ask the user for a short sentence and build a dictionary that counts how many times each word appears.

3. **Unique numbers with sets**  
   Ask the user to enter numbers (separated by spaces), store them in a set, and show how many unique numbers there are.

