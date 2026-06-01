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
#     print(f_contents)  # readline() reads the file line by line and returns a STRING of the current line

# with open("test.txt", "r") as f:
#     for line in f:
#         print(line, end='')  # This will print each line of the file, including the newline character at the end of each line

# with open("test.txt", "r") as f:
#     f_contents = f.read(100)  # read() reads the file and returns a STRING of the entire file or up to the specified number of characters
#     print(f_contents, end='')

#     f_contents = f.read(100)  # This will read the next 100 characters from the file, starting from where the previous read left off
#     print(f_contents, end='') # end='' is used to prevent adding an additional newline character after printing the contents.


with open("test.txt", "r") as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents, end='')

    # seek() is used to move the file pointer to a specific position in
    # the file. In this case, it moves the pointer back to the beginning
    # of the file (position 0).
    f.seek(0)
    f_contents = f.read(size_to_read)
    print(f_contents)

    # # tell() returns the current position of the file pointer,
    # # which is the number of characters read from the file so far.
    # print(f.tell())

    # # This loop will continue to read the file in chunks of 100 characters
    # # until the end of the file is reached. The loop will terminate when
    # # f_contents is an empty string, which indicates that there are no
    # # more characters to read from the file.
    # while len(f_contents) > 0:
    #     f_contents = f.read(size_to_read)
    #     print(f_contents, end='')
