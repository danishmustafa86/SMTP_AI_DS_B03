# LESSON 7: *args and **kwargs
# Handle unlimited arguments

# === *args - Multiple Positional Arguments ===
# Collects extra arguments into a TUPLE
def add_all(*args):
    print(f"Received: {args}")
    return sum(args)

print(add_all(1, 2))
print(add_all(1, 2, 3, 4, 5))

# === Mixing Regular + *args ===
def greet_all(greeting, *names):
    for name in names:
        print(f"{greeting}, {name}!")

greet_all("Hello", "Ali", "Sara", "Ahmed")

# === **kwargs - Multiple Keyword Arguments ===
# Collects extra keyword args into a DICTIONARY
def print_info(**kwargs):
    print(f"Received: {kwargs}")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print_info(name="Ali", age=25, city="Dubai")

# === Combining All Types ===
# Order: regular, *args, **kwargs
def super_func(required, *args, **kwargs):
    print(f"Required: {required}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

super_func("Hello", 1, 2, 3, "danish", name="Ali", age=25)
