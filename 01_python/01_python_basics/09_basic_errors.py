# We study basic errors so we can quickly find bugs and make our programs more reliable.
# Examples of common syntax errors and runtime errors.


# print("This file shows examples of common Python errors.")

# ----------------------
# Syntax error examples
# ----------------------

# 1) Missing closing parenthesis
# print("Hello, World!")   # SyntaxError: '(' was never closed

# # 2) Wrong indentation
# # print("Bad indent")   # IndentationError

# # ----------------------
# # Runtime error examples
# # ----------------------

# # 3) ZeroDivisionError
# # print("ZeroDivisionError")
# # print("--------------------------------", 23 + 23)
# # result = 10 / 0
# # print(result)

# # 4) TypeError - mixing incompatible types
# num1 = input("please enter you first number: ")
# num2 = input("please enter you second number: ")
# num3 = int(num1)
# print(type(num3),  "num 2 tupe ", type(num2))
# total = num3 + num2
# print(total)
# total = 10 + "10"
# print(total)

# 5) ValueError - invalid conversion
number = int("10a")
print(number)

# print("Run this file, then uncomment one error example to see what happens.")
