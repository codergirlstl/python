#Final python project for savvycoders
#import modules
import os

#Declare an empty renamelist
renamelist =[]

path=input("Please specify a directory using the relative path: ")
filename =str(path)
print(filename)

for subdir, dirs, files in os.walk(filename):
    for file in files:
        filepath = subdir + os.sep + file
        renamelist.append(str(filepath))

#Rename file
#os.rename(source, dest)
