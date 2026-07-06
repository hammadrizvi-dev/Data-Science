# File handling example
# Python can read and write files.

with open("demo_file.txt", "w") as file:
    file.write("Hello from Python")

with open("demo_file.txt", "r") as file:
    print("File content:", file.read())

with open("demo_file.txt", "a") as file:
    file.write("\nThis is appended text")
