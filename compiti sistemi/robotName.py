import random
import string
string.ascii_uppercase

def robotName():
    stringName = ""
    for _ in range (0, 2):
        stringName += random.choice(string.ascii_uppercase)

    for _ in range (0, 3):
        stringName += str(random.randint(0, 9))

    return stringName

print(robotName())