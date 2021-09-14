def allYourBase(num, base):
    final = 0
    cnt = len(str(num))-1
    for n in str(num):
        final += int(n) * base**cnt
        cnt -= 1
    
    return final


print(allYourBase(1120, 3))