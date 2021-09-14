def rotational_cipher(string, offset):
    string = string.lower()
    strRot = ""
    for element in string:
        if element == " ":
            strRot = strRot + element
        else:
            element = ord(element) - ord('a')       #ord da il codice asci della lettera
            element = (element + offset) % 26
            element = element + ord('a')
            element = chr(element)
            strRot = strRot + element
    return strRot

print("abcdefghijklmnopqrstuvwxyz")
print(rotational_cipher("abcdefghijklmnopqrstuvwxyz", 13))