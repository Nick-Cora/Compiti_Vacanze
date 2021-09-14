def acronym(string_acro):

    acronym_final = ""
    for word in string_acro.split(" "):
        acronym_final += word[0].upper()
    return acronym_final

print(f"The acronym is: {acronym('Three Letter Acronyms')}")