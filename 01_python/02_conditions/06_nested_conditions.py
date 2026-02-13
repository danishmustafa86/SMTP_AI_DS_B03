"""Nested conditions (if inside if)

Sometimes we need to check one condition, and then inside that,
check another condition. This is called nesting.

Example:
- First check: "Is user logged in?"
- Second check: "Is user an admin?"
"""

# is_logged_in = True
# is_admin = False

# if is_logged_in == True:
#     if is_admin == True:
#         print("you are admin, and you have admin access")
#     else:
#         print("you are normal student, are you have just view acces")
# else:
#     print("you cannot have access to our website")


# Real-world style example:
# Online store discount only for logged-in students
# is_logged_in = True
# is_student = True

# if is_logged_in:
#     print("User is logged in.")

#     if is_student:
#         print("Student discount applied!")
#     else:
#         print("No student discount. Regular prices apply.")
# else:
#     print("Create an account or log in to see discounts.")


