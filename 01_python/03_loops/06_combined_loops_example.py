"""Combined loops – realistic scenarios

This file puts together:
- for loops
- while loops
- range()
- break and continue
- nested loops
- conditions and operators

Examples: Easy to Medium difficulty combining multiple concepts
"""

# ============================================
# EXAMPLE 1: Number validator with while + break
# ============================================
print("EXAMPLE 1: Validate user input (1-100)")
print("=" * 40)

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    number = int(input("Enter a number between 1 and 100: "))
    attempts += 1
    
    if number >= 1 and number <= 100:
        print(f"Valid number: {number}")
        break
    else:
        print(f"Invalid! You have {max_attempts - attempts} attempts left.")
        
    if attempts == max_attempts:
        print("Too many invalid attempts!")

print("\n" + "=" * 40 + "\n")

# ============================================
# EXAMPLE 2: Sum calculator with continue
# ============================================
print("EXAMPLE 2: Sum positive numbers only")
print("=" * 40)

total = 0
count = 0

for i in range(1, 11):
    number = int(input(f"Enter number {i} (can be negative): "))
    
    if number < 0:
        print("Negative number skipped!")
        continue  # skip negative numbers
    
    total += number
    count += 1
    print(f"Running sum: {total}")

print(f"Total of {count} positive numbers: {total}")

print("\n" + "=" * 40 + "\n")

# ============================================
# EXAMPLE 3: Find first number with condition (for + break)
# ============================================
print("EXAMPLE 3: Find first number divisible by 7 and 9")
print("=" * 40)

found = False

for num in range(1, 200):
    if num % 7 == 0 and num % 9 == 0:
        print(f"Found: {num}")
        found = True
        break

if not found:
    print("No number found!")

print("\n" + "=" * 40 + "\n")

# ============================================
# EXAMPLE 4: Multiplication table printer (nested loops)
# ============================================
print("EXAMPLE 4: Multiplication table 5x5 with skip")
print("=" * 40)

for i in range(1, 6):
    for j in range(1, 6):
        result = i * j
        
        # Skip multiples of 5 except 5 and 25
        if result % 5 == 0 and result != 5 and result != 25:
            continue
            
        print(f"{i}×{j}={result:2}", end="  ")
    print()  # new line

print("\n" + "=" * 40 + "\n")

# ============================================
# EXAMPLE 5: Password system with multiple conditions
# ============================================
print("EXAMPLE 5: Login system (3 attempts)")
print("=" * 40)

correct_password = "python123"
max_tries = 3
tries = 0

while tries < max_tries:
    password = input("Enter password: ")
    tries += 1
    
    if password == correct_password:
        print("✓ Login successful!")
        break
    else:
        remaining = max_tries - tries
        if remaining > 0:
            print(f"✗ Wrong password. {remaining} attempts left.")
        else:
            print("✗ Account locked! Too many attempts.")

print("\n" + "=" * 40 + "\n")

# ============================================
# EXAMPLE 6: Counter with while + multiple conditions
# ============================================
print("EXAMPLE 6: Count to 50 (skip multiples of 3 and 5)")
print("=" * 40)

number = 1
count_printed = 0

while number <= 50:
    if number % 3 == 0 or number % 5 == 0:
        number += 1
        continue  # skip multiples of 3 or 5
    
    print(number, end=" ")
    count_printed += 1
    number += 1

print(f"\nTotal numbers printed: {count_printed}")

print("\n" + "=" * 40 + "\n")

# ============================================
# EXAMPLE 7: Calculate average with validation
# ============================================
print("EXAMPLE 7: Calculate average of valid scores")
print("=" * 40)

total_score = 0
valid_count = 0

for i in range(1, 6):
    score = int(input(f"Enter score {i} (0-100): "))
    
    if score < 0 or score > 100:
        print("Invalid score! Skipped.")
        continue
    
    total_score += score
    valid_count += 1

if valid_count > 0:
    average = total_score / valid_count
    print(f"Average of {valid_count} valid scores: {average:.2f}")
else:
    print("No valid scores entered!")

print("\n" + "=" * 40 + "\n")

# ============================================
# EXAMPLE 8: Prime number checker (nested loop + break)
# ============================================
print("EXAMPLE 8: Check if a number is prime")
print("=" * 40)

number = int(input("Enter a number to check: "))

if number < 2:
    print(f"{number} is not prime")
else:
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            print(f"{number} is divisible by {i}")
            is_prime = False
            break  # found a divisor, no need to continue
    
    if is_prime:
        print(f"{number} is a prime number!")
    else:
        print(f"{number} is not prime")

print("\n" + "=" * 40 + "\n")

# ============================================
# EXAMPLE 9: Pattern with conditions (nested loops)
# ============================================
print("EXAMPLE 9: Number pattern with conditions")
print("=" * 40)

rows = 5

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        # Print only odd numbers
        if j % 2 == 0:
            continue
        print(j, end=" ")
    print()

print("\n" + "=" * 40 + "\n")

# ============================================
# EXAMPLE 10: Sum with break condition
# ============================================
print("EXAMPLE 10: Sum numbers until total exceeds 100")
print("=" * 40)

total = 0
number = 1

while True:
    total += number
    print(f"Adding {number}, total = {total}")
    
    if total > 100:
        print("Total exceeded 100! Stopping.")
        break
    
    number += 1

print(f"Final total: {total}")

print("\n" + "=" * 40)
print("All combined loop examples completed!")
print("=" * 40)


# ============================================
# Practice Examples (add your solutions below):
# ============================================
# 1. Create a countdown timer from 10 to 1, skip numbers divisible by 3
# 2. Ask user for 5 numbers, calculate sum but skip any number greater than 50
# 3. Print all numbers from 1-100 that are divisible by both 4 and 6
# 4. Create a pattern: print stars increasing then decreasing (1,2,3,4,3,2,1)
# 5. Find the sum of all even numbers between 1-100, stop when sum exceeds 500
