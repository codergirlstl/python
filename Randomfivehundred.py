#Generate a list of 500 random numbers using a loop and print them to a text file. It can be a text blob or one value per line
import random

#create an empty list
numberlist = []
#declare a count variable to use in loop
count = 0
#use a for loop to generate 500 random numbers
while count < 501:
    random_number=random.randint(0,9)
    numberlist.append(random_number)
    count+=1

#print the numbers to a text file
textfile = open("numberfile.txt", "w")
for element in numberlist:
    textfile.write(str(element))
textfile.close()
print("You did it!")
