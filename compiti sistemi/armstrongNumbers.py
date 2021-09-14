def armstrongNumber(num):
    sumNum = 0

    for k in str(num):
        sumNum += int(k)**len(str(num))
    
    if num == sumNum:
        return True, num, sumNum
    else:
        return False, num, sumNum

print(armstrongNumber(153))