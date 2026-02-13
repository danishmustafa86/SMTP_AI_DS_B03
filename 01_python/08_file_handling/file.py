# file = open("practice.txt", "r")
# print(file.read())
# file.close()


# file = open('practice.txt', '')
# file.write("Hello Danish")
# file.close()


# file = open('practice.txt', 'a')
# file.write("\nHello Danish")
# file.close()



# file = open("newfile.txt", "x")
# file.write("New file created")
# file.close()

# file = open("practice.txt", "r")
# print(file.read(100))
# file.close()


# file = open("practice.txt", "r")
# print(file.readline())
# print(file.readline())
# file.close()



# file = open("practice.txt", "r")
# print(file.read())
# file.close()

# file = open("practice.txt", "r")
# print(file.readlines())
# file.close()

# file = open("data.txt", "w")
# file.writelines(["Line 1\n", "Line 2\n", "Line 3"])
# file.close()


# file = open("data.txt", "r")
# print(file.tell())
# print(file.read(5))
# print(file.read(5))
# print(file.tell())
# file.close()


# file = open("data.txt", "r")
# file.seek(30)
# print(file.read())
# file.close()


with open("indexes.txt", "w") as file:
    for i in range(1, 101):
        file.write(f"Index {i}\n")

# with open("indexes.txt", "r") as file:
#     for line in file:
#         print(line)

# with open("indexes.txt", "a") as file:
#     file.write("Index 101\n")

# with open("indexes.txt", "r") as file:
#     print(file.read())


with open("README.md", "rb") as file:
    counter = 0
    for line in file:
        counter += 1
    print(counter)