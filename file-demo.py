# # 'test2.txt will be created if it does not exist,
# # and if it does exist, it will be overwritten with
# # the new content.'
# with open("test2.txt", 'w') as f:
#     f.write("This is a test file.\n")
#     f.write("It contains multiple lines of text.\n")


# # # 'test_copy.txt will be created if it does not exist,
# # # and if it does exist, it will be overwritten with the content of test.txt.'
# with open("test.txt", 'r') as rf:
#     with open("test_copy.txt", 'w') as wf:
#         for line in rf:
#             wf.write(line)


# # 'crimson-desert.png will be copied to crimson-desert_copy.png.
# # The 'rb' mode is used to read the file in binary mode,
# # and the 'wb' mode is used to write the file in binary mode.
# # This is necessary for copying binary files such as images.'
# with open("crimson-desert.png", 'rb') as rf:
#     with open("crimson-desert_copy.png", 'wb') as wf:
#         for line in rf:
#             wf.write(line)


# The above code reads the image file in chunks of 1024 bytes
# and writes each chunk to the new file. This is more efficient 
# than reading and writing the entire file at once, especially 
# for large files.
with open("crimson-desert.png", 'rb') as rf:
    with open("crimson-desert_copy.png", 'wb') as wf:
        chunk_size = 1024
        while len(chunk := rf.read(chunk_size)) > 0:
            wf.write(chunk)
