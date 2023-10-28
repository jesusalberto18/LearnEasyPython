# Getting the current working directory
import os

cwd = os.getcwd()

print(cwd)


# Changing the current working directory
import os

os.chdir("/path/to/new/directory")


# Creating a directory
import os

os.mkdir("new_directory")


# Removing a directory
import os

os.rmdir("new_directory")


# Checking if a file exists
import os

if os.path.exists("myfile.txt"):
    print("The file exists!")
else:
    print("The file does not exist.")


# Opening a file
import os

f = open("myfile.txt", "r")

contents = f.read() #read the contents of the file

f.close() #close the file

