def raindrops(num):
    res = ""
    if num % 3 == 0:
        res += "Pling"

    if num % 5 == 0:
        res += "Plang"

    if num % 7 == 0:
        res += "Plong"
        
    if res == "":
        res = num

    return res

def main():
    x = int(input("Enter number... "))
    print(raindrops(x))


if __name__ == "__main__":
    main()
