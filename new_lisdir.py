import os
import os.path
# Get the path from the user
path = input(str("Please give me a directory path for this program:"))
# Get the list of all files and directories

# in current working directory
dir_list = os.listdir(path)

print("Files and directories in '", path, "' :")
# print the list
print(dir_list)
