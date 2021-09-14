def twoFer(name):
    if name != "":
        return f"One for {name}, one for me"
    else:
        return f"One for you, one for me"

def main():
    x = input("Enter name... ")
    print(twoFer(x))


if __name__ == "__main__":
    main()