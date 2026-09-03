# Random Game Number Project

import random
cNumber = random.randrange(1,101)
userInput = int(input("Enter the Number :"))

if userInput>cNumber:
    print("computer number is:",cNumber)
    print("your guess number is too high")
elif cNumber>userInput:
    print("computer number is:",cNumber)
    print("your guess number is too low")
else:
    print("computer number is:",cNumber)
    print("your guess number is equal")        