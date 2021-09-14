def isogram(word):
    lettList = []
    for letter in word.lower():
        if letter in lettList:
            return False
        if letter > 'a' and letter < 'z':
            lettList.append(letter)
    return True


print(isogram("background"))