"""WAP to read data from keyboard &
write it to the file. After writing is
completed, the file is closed. The
program again opens the same file
and reads it.
"""

text_file = open("readme.txt","w")
text_file.write("Hello\n")
text_file.write("I'm Learning Python\t")
text_file.write("Bye!")
text_file.close()


file = open("readme.txt","r")

for line in file:
    print(line)


