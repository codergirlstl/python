import os
import os.path

directory_path = os.getcwd()
print("My current directory is : " + directory_path)
folder_name = os.path.basename(directory_path)
print("My directory name is : " + folder_name)
print("The files listed under "+ folder_name + " are: ")
directory_files=os.listdir(directory_path)
print(directory_files)
