"""Basic while loop

We use while loops to repeat an action WHILE a condition is True.
Be careful to update the condition, otherwise you get an infinite loop.

Examples:
- Ask for a password until it is correct
- Count up until a limit
"""


# print("Counting up with while loop:")

# count = 1
# while count <= 5:
#     print("Count =", count)
#     # count += 1  # update the variable so the loop can stop









# print("--------------------------------")

# print("Simple login attempt example:")

# correct_password = "python123"
# password = input("Enter password: ")

# while password != correct_password:
#     print("Wrong password. Try again.")
#     password = input("Enter password: ")

# print("Login successful!")


# Practice Examples (add your solutions below):
# 1. Keep doubling a number starting from 1 until it exceeds 1000
# number = 1
# while number <= 1000:
#     print(number)
#     number = number * 2
# print("Final number:", number)

# # 2. Ask user for a positive number, keep asking until they enter one
# num = int(input("Enter a positive number: "))
# while num <= 0:
#     print("That's not positive!")
#     num = int(input("Enter a positive number: "))
# print("You entered:", num)

# # 3. Calculate factorial of a number using while loop
# 20!  
# !5 = 5*4*3*2*1
# num = input("enter number which you wanna factorial ")
# num = int(num)
# num2 = 1
# factorial = 1 

# while num2 <= num:
#     print("current number is ", num2)
#     factorial *= num2
#     print("currently factorial of number ", num2, " is ", factorial)
#     num2 += 1

# factorial = 1*1     => num2 = 1, factorial = 1 ans=1
# factorial = 1 * 2   => num2 = 2, factorial = 1 ans = 2
# factorial = 2 * 3   => num2 = 3, factorial = 2 ans= 6
# factorial = 6 * 4   => num2 = 4, factorial = 6 ans = 24
# factorial = 24 * 5   => num2 = 5, factorial = 24 ans = 120






# factorial = 1
# counter = 1
# while counter <= n:
#     factorial = factorial * counter
#     counter = counter + 1
# print("Factorial of", n, "is", factorial)

# 4. Keep asking for password (max 3 attempts) using a counter
# secret = "admin123"
# attempts = 0
# user_pass = input("Enter password: ")

# while user_pass != secret and attempts < 2:
#     attempts = attempts + 1
#     print("Wrong! Attempts left:", 3 - attempts)
#     user_pass = input("Enter password: ")

# if user_pass == secret:
#     print("Access granted!")
# else:
#     print("Account locked!")

# # 5. Find the first number divisible by 7 and 13 between 1-500
num = 1
while num <= 500:
    if num % 7 == 0 and num % 13 == 0:
        print("First number divisible by 7 and 13 is:", num)
        break
    num = num + 1
