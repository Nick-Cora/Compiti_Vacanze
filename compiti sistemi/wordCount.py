word_value = {}

def wordCount(string):
    for word in string.split():
        word = word.lower()
        if not word in word_value:
            word_value[word] = 1
        else:
            word_value[word] += 1

    return word_value


def main():
    x = str(input("Enter phrase..."))

    print(wordCount(x))


if __name__ == "__main__":
    main()