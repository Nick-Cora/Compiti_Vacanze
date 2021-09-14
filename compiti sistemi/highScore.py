def highScore(lis):
    last = lis[-1]
    max_score = max(lis)
    if len(lis) < 3:
        raise Exception("not enough list items")
    else:
        three_max = []
        while len(three_max) < 3:
            three_max.append(max(lis))
            lis.remove(max(lis))

    return (f"Last score: {last} \nMax score: {max_score} \nTop 3 max score: {three_max}")

def main():
    lista=[]
    x = int(input("Enter score, enter '-1' to finish... "))

    while x != -1:
        lista.append(x)
        x = int(input("Enter score, enter '-1' to finish... "))

    print(highScore(lista))


if __name__ == "__main__":
    main()