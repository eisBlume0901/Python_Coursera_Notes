
# r is for reading, w is for writing, a is for appending
aboutPythonFile = open("about_python.txt", "r")

print("Name of the file: ", aboutPythonFile.name) # Returns about_python.txt
print("Mode of the file: ", aboutPythonFile.mode) # Returns r means readable

aboutPythonFile.close()

# Alternative 1 for opening and closing the file without using with statement (it reads the contents of the txt file without creating a new line every after a line)
# Advantages: automatic resource management (will close even an exception occurs), cleaner and more concise code (readable and less-error prone)
with open("about_python.txt", "r") as aboutPythonFile:
    file_contents = aboutPythonFile.read() # Prints the contents of the file
    print(file_contents)

print("Is it closed? ", aboutPythonFile.closed) # Returns a boolean value if the file is closed which is expected to be closed\
print(file_contents) # Still can access the contents of the file despite the file being closed already

# Reading one line per new line "\n"
with open("about_python.txt", "r") as aboutPythonFile:
    first_sentence = aboutPythonFile.readline() # Note the sample text must indent new line each entry
    print(first_sentence)

with open("about_python.txt", "r") as aboutPythonFile:
    file_contents = aboutPythonFile
    print(file_contents) # <_io.TextIOWrapper name='about_python.txt' mode='r' encoding='cp1252'>

# Reading a string returned by the readline
with open("about_python.txt", "r") as aboutPythonFile:
    first_word = aboutPythonFile.readline(6)
    print(first_word) # Returns "Python"
    second_word = aboutPythonFile.readline(3)
    print(second_word) # Returns "is" (note it does not return the second line word but still at the first line
    third_word = aboutPythonFile.readline(3)
    print(third_word) # Returns "a"
    fourth_word = aboutPythonFile.read(5) # Returns "high-"
    print(fourth_word)

# Reading every line inside the text file using while loop
with open("about_python.txt", "r") as aboutPythonFile:
    while True:
        line = aboutPythonFile.readline()
        if not line:
            break
        print(line) # Returns each line with

# Reading ever line inside the text file using for loop
with open("about_python.txt", "r") as aboutPythonFile:
    i = 0
    for line in aboutPythonFile:
        print("Iteration", str(i), ": ", line)
        i = i + 1

# Using other file methods
with open("about_python.txt", "r") as aboutPythonFile:
    aboutPythonFile.seek(6) # Moves the 0th index as 11,
    file_contents = aboutPythonFile.readline()
    print(file_contents)

