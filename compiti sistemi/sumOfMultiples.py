def sumOfMultiples(numberRange):
    listMultiples = []
    for count in range(1, numberRange):
        if count % 3 == 0 or count % 5 == 0:
            listMultiples.append(count)
    return listMultiples, sum(listMultiples)


def main():
    x = int(input("Enter a range number..."))

    print(sumOfMultiples(x))


if __name__ == "__main__":
    main()