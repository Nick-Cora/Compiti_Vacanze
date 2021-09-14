def transpose(r1, r2):
    string_final = ""

    if len(r1) > len(r2):
        r2 += "/"
        
    elif len(r2) > len(r1):
        r1 += "/"

    for count in range(len(r1)):
        string_final += r1[count] + r2[count] + "\n"

    return string_final


print(transpose("ab", "def"))