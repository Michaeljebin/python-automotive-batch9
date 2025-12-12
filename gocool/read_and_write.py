with open("example.txt", "w") as file:
    file.write("Hello, this is a test file.\n")
    file.write("Python file handling is easy!")

# Reading from the file
with open("example.txt", "r") as file:
    content = file.read()

print("File content:")
print(content)