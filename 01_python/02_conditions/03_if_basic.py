"""Basic if statement

We use if statements to run code ONLY when a condition is True.
Example questions:
- "Is the user an adult?"
- "Is the temperature too high?"
"""

age = 20

print("Age:", age)

# Simple condition: check if the user is an adult
if age >= 18:
    print("You are an adult.")

print("This line always runs, no matter the age.")

print("--------------------------------")

# Real-world style example: warning if battery is low
battery_percentage = 15
print("Battery:", battery_percentage, "%")

if battery_percentage < 20:
    print("Warning: Battery is low. Please charge your device.")

print("Program finished.")


