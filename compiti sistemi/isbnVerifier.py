def isbnVerifier(isbn):
    sumNum = 0
    numString = ""
    count = 10

    if "-" in isbn:
        numStringApp = str(isbn).split("-")

        for k in numStringApp:
            numString += k
    else:
        numString = isbn

    for i in range (0, len(numString)):
        sumNum += int(numString[i]) * count
        count -= 1
    
    if sumNum % 11 == 0:
        return True
    else:
        return False
    
print(isbnVerifier("3-598-21508-8"))