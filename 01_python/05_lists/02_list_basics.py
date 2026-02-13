# 02_list_basics.py - Creating and accessing lists

# Creating lists
numbers = [10, 20, 30, 40]
fruits = ["apple", "banana", "cherry"]

# Indexing (starts from 0)
print(fruits[0])    # apple (first)
print(fruits[-1])   # cherry (last)


# Change item
fruits[0] = "mango"
print(fruits)       # ['mango', 'banana', 'cherry']

# Length
print(len(fruits))  # 3

# Add items
fruits.append("orange")      # add to end
fruits.insert(1, "grape")    # insert at position

# Remove items
fruits.remove("banana")      # remove by value
fruits.pop()                 # remove last
print(fruits)
