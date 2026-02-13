"""
File Handling Practice Examples
5 Practical Examples to Master File Operations in Python
"""

# =============================================================================
# EXAMPLE 1: Creating and Writing to a New File
# =============================================================================
print("=" * 60)
print("EXAMPLE 1: Writing to a New File")
print("=" * 60)

# Create a new file and write student information
file = open("example1_students.txt", "w")
file.write("Student Name: Alice\n")
file.write("Student ID: 101\n")
file.write("Grade: A\n")
file.write("Course: Python Programming\n")
file.close()

print("✓ File 'example1_students.txt' created successfully!")
print()


# =============================================================================
# EXAMPLE 2: Reading File Content (Multiple Methods)
# =============================================================================
print("=" * 60)
print("EXAMPLE 2: Reading File Content")
print("=" * 60)

# Method 1: Read entire file at once
file = open("example1_students.txt", "r")
content = file.read()
print("Method 1 - Read entire file:")
print(content)
file.close()

print("-" * 40)

# Method 2: Read line by line
file = open("example1_students.txt", "r")
print("Method 2 - Read line by line:")
for line in file:
    print(f"  → {line.strip()}")
file.close()
print()


# =============================================================================
# EXAMPLE 3: Appending Data to an Existing File
# =============================================================================
print("=" * 60)
print("EXAMPLE 3: Appending to a File")
print("=" * 60)

# Append more student records
file = open("example1_students.txt", "a")
file.write("\n--- New Student Added ---\n")
file.write("Student Name: Bob\n")
file.write("Student ID: 102\n")
file.write("Grade: B+\n")
file.write("Course: Python Programming\n")
file.close()

print("✓ New student record appended!")

# Read and display the updated file
file = open("example1_students.txt", "r")
print("\nUpdated file content:")
print(file.read())
file.close()
print()


# =============================================================================
# EXAMPLE 4: Processing and Transforming File Data
# =============================================================================
print("=" * 60)
print("EXAMPLE 4: Processing File Data")
print("=" * 60)

# Create a file with numbers
file = open("example4_numbers.txt", "w")
numbers = [10, 25, 30, 45, 50, 15, 20]
for num in numbers:
    file.write(f"{num}\n")
file.close()

print("✓ Created file with numbers:", numbers)

# Read numbers, calculate statistics, and save results
file = open("example4_numbers.txt", "r")
number_list = []
for line in file:
    number_list.append(int(line.strip()))
file.close()

# Calculate statistics
total = sum(number_list)
average = total / len(number_list)
maximum = max(number_list)
minimum = min(number_list)

# Save statistics to a new file
file = open("example4_statistics.txt", "w")
file.write("=" * 40 + "\n")
file.write("     STATISTICS REPORT\n")
file.write("=" * 40 + "\n")
file.write(f"Numbers: {number_list}\n")
file.write(f"Total: {total}\n")
file.write(f"Average: {average:.2f}\n")
file.write(f"Maximum: {maximum}\n")
file.write(f"Minimum: {minimum}\n")
file.write("=" * 40 + "\n")
file.close()

print("✓ Statistics calculated and saved to 'example4_statistics.txt'")

# Display the statistics file
file = open("example4_statistics.txt", "r")
print("\nStatistics Report:")
print(file.read())
file.close()
print()


# =============================================================================
# EXAMPLE 5: Using Context Manager (with statement) - Best Practice!
# =============================================================================
print("=" * 60)
print("EXAMPLE 5: Using Context Manager (Recommended Method)")
print("=" * 60)

# Create a shopping list
shopping_items = [
    "Apples - $3.50",
    "Bread - $2.00",
    "Milk - $4.25",
    "Eggs - $3.75",
    "Cheese - $5.50"
]

# Using 'with' statement - automatically closes the file
with open("example5_shopping.txt", "w") as file:
    file.write("=" * 40 + "\n")
    file.write("    MY SHOPPING LIST\n")
    file.write("=" * 40 + "\n\n")
    for item in shopping_items:
        file.write(f"• {item}\n")
    file.write("\n" + "=" * 40 + "\n")

print("✓ Shopping list created using context manager!")

# Read and process the shopping list
with open("example5_shopping.txt", "r") as file:
    print("\nShopping List Content:")
    for line in file:
        print(f"  {line.rstrip()}")

# Calculate total cost from shopping list
total_cost = 0
with open("example5_shopping.txt", "r") as file:
    for line in file:
        if "$" in line:
            # Extract price from line
            price = float(line.split("$")[1].strip())
            total_cost += price

print(f"\n💰 Total Shopping Cost: ${total_cost:.2f}")
print()


# =============================================================================
# PRACTICE CHALLENGES
# =============================================================================
print("=" * 60)
print("🎯 PRACTICE CHALLENGES FOR YOU!")
print("=" * 60)
print("""
1. Create a file 'diary.txt' and write 3 diary entries with dates.

2. Read 'example1_students.txt' and count how many students have grade 'A'.

3. Create a file with 10 product names and prices, then read it and 
   find the most expensive product.

4. Write a program that reads 'test.txt' and counts:
   - Total lines
   - Total words
   - Total characters

5. Create a contact list file with names and phone numbers, then 
   search for a specific person's phone number.

TIP: Always use 'with' statement for file operations - it's safer!
""")
print("=" * 60)
print("🎓 Happy Learning!")
print("=" * 60)

