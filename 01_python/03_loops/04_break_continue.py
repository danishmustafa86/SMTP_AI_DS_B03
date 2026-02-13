"""break and continue in loops

We use:
- break    -> to stop the loop early
- continue -> to skip the rest of this loop step and go to the next one

Examples:
- Stop searching when we find what we want
- Skip invalid data and continue with the rest
"""

print("Searching for number 7 in a list:")

numbers = [1, 3, 7, 9, 11]

for n in numbers:
    print("Checking:", n)
    if n == 7:
        print("Found 7! Stopping search.")
        break  # exit the loop when we find 7

print("--------------------------------")

print("Printing only odd numbers using continue:")

for n in range(1, 10):
    if n % 2 == 0:
        continue  # skip even numbers
    print("Odd number:", n)

print("Loop finished.")


# Practice Examples (add your solutions below):
# 1. Find and print the first perfect square greater than 100, then stop
# 2. Print numbers 1-30 but skip all multiples of 4 using continue
# 3. Check if a number is prime (stop checking when you find a divisor)
# 4. Sum only odd numbers from 1-50, skip even numbers with continue
# 5. Create a number guessing game (1-10) that breaks on correct guess
