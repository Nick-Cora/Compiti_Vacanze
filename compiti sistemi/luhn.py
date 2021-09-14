def luhn(numCard):
    sumNum = 0
    tempNum = str(numCard).split(" ")

    if len(tempNum) != 4:
        return False

    stringNum = ""

    for x in tempNum:
        stringNum += x

    for x in range(0, len(stringNum)):
        if x % 2 == 0:

            if int(stringNum[x]) * 2 > 9:
                sumNum += (int(stringNum[x]) * 2) - 9
            else:
                sumNum += int(stringNum[x]) * 2

        else:
            sumNum += int(stringNum[x])


    if sumNum % 10 == 0:
        return True
    else:
        return False

print(luhn("8273 1232 7352 0569"))