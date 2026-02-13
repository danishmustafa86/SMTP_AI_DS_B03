# 03_list_loops.py - Looping through lists

fruits = ["apple", "banana", "cherry"]

# Simple loop
for fruit in fruits:
    print(fruit)



# Calculate with loop
scores = [85, 90, 78, 92]
total = 0
for s in scores:
    total += s
print("Average:", total / len(scores))

# Filter items
nums = [5, 12, 3, 18, 7]
big = [n for n in nums if n > 10]
print("Numbers > 10:", big)
