def reverseString(string):
    rev_string = ""
    cont = len(string) - 1

    while cont >= 0:
        rev_string += string[cont]
        cont = cont - 1
#.reverse
    return rev_string

print(reverseString("cavallo"))