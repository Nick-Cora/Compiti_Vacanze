letter_values = {
    'a':1, 'A':1,
    'e':1, 'E':1,
    'i':1, 'I':1,
    'o':1, 'O':1,
    'u':1, 'U':1,
    'l':1, 'L':1,
    'n':1, 'N':1,
    'r':1, 'R':1,
    's':1, 'S':1,
    't':1, 'T':1,

    'd':2, 'D':2,
    'g':2, 'G':2,

    'b':3, 'B':3,
    'c':3, 'C':3,
    'm':3, 'M':3,
    'p':3, 'P':3,

    'f':4, 'F':4,
    'h':4, 'H':4,
    'v':4, 'V':4,
    'w':4, 'W':4,
    'y':4, 'Y':4,

    'k':5, 'K':5,

    'j':8, 'J':8,
    'x':8, 'X':8,

    'q':10, 'Q':10,
    'z':10, 'Z':10
}

def scrabbleScore(word):
    score = 0

    for letter in word:
        score += letter_values[letter]
    return (f"Word: {word}\t Score: {score}")


def main():
    x = str(input("Enter word..."))

    print(scrabbleScore(x))


if __name__ == "__main__":
    main()