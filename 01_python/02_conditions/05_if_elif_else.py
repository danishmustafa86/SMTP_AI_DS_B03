"""if / elif / else: multiple choices

We use if/elif/else to pick ONE matching option from several.
Real-life examples:
- Assigning a grade (A, B, C, D, F)
- Choosing a ticket price based on age groups
"""

# Real-world style example: cinema ticket price based on age
# age = 10


marks = input("Enter your marks: ")
marks = int(marks)


if marks >= 90:
    print("A+ Grage")
elif marks >= 80:
    print("A grade")
elif marks >= 70:
    print("B grade")
elif marks >= 60:
    print("C grade")
elif marks >= 50:
    print("D grade")
else:
    print("Congratilations, you are fail")




# print("Age:", age)

# if age < 12:
#     price = 5  # child price
# elif age <= 60:
#     price = 10  # standard adult price
# else:
#     price = 7  # senior price

# print("Ticket price:", price, "USD")


