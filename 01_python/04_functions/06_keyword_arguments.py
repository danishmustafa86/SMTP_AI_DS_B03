# LESSON 6: Keyword Arguments
# Specify which parameter gets which value using name=value

# === Positional vs Keyword ===
def describe(animal, name, age):
    print(f"A {animal} named {name}, {age} years old")

# Positional (order matters)
describe("cat", "Mimi", 3)

# Keyword (order doesn't matter)
describe(name="Buddy", age=5, animal="dog")
describe(age=2, animal="bird", name="Tweety")

# === Mixing (positional first, then keyword) ===
def create_user(username, email, role="user", active=True):
    print(f"{username} | {email} | {role} | Active: {active}")

create_user("ali", "ali@email.com")
create_user("sara", "sara@email.com", role="admin")
create_user("ahmed", "ahmed@email.com", active=False)
