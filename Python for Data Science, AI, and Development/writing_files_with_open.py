

with open("learning_with_file_writing.txt", "w") as file:
    file.write("Learning Python's file writing functionality\n")

with open("learning_with_file_writing.txt", "a") as file:
    contents = ["There are 3 different modes with file",
                "1. r means to read the file contents",
                "2. w means to write something in file contents",
                "3. a means to append an existing file with contents with new contents"]
    for line in contents:
        file.write(line + "\n") # Every line written there is a new line after it

# nesting with with-statement, good for copying existing file to another file
with open("about_file_writing.txt", "r") as sourceFile:
    with open("learning_with_file_writing.txt", "a") as destinationFile: # destination file
        for line in sourceFile:
            destinationFile.write(line)


with open("learning_with_file_writing.txt", "r+") as file:
    contents = file.read()
    print(contents)
    file.write("\n" + "Furthermore, there are also combinations of modes.")

with open("learning_with_file_writing.txt", "a+") as file:
    file.write("\n" + "Examples include r+, w+, a+, x+")
    file.seek(0)
    contents = file.read()
    print(contents)

try:
    with open('learning_with_file_writing.txt', 'x+') as file:
        file.write('Content for new file')  # Write to the file
        file.seek(0)  # Move the read/write location to the start of the file
        content = file.read()  # Read the file
except FileExistsError:
    print('File already exists')