# f = open("test.txt", "r")
# print("File mode:", f.mode)
# print("File name:", f.name)
# print(f.read())
# f.close()

# # Benefit of using 'with' statement is that it automatically closes the file
# # after the block of code is executed, even if an error occurs. This helps
# # to prevent resource leaks and ensures that the file is properly closed.
# with open("test.txt", "r") as f:
#     print("File mode:", f.mode)
#     print("File name:", f.name)
#     print(f.read())

# with open("test.txt", "r") as f:
#     f_contents = f.readlines()
#     print(f_contents)  # readlines() reads the file line by line and returns a LIST of lines
#     f_contents = f.readline()
#     print(f_contents) # readline() reads the file line by line and returns a STRING of the current line

with open("test.txt", "r") as f:
    for line in f:
        print(line, end='')  # This will print each line of the file, including the newline character at the end of each line
