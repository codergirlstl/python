#input all the letters in your full name and scramble them
import random

full_name = input(str("Please give me your full name: "))
print(full_name)


newname = list(full_name)
random.shuffle(newname)
result = ''.join(newname)
print(result)
