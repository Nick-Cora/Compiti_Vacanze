from math import sqrt


def score(x, y):
    dist = sqrt(x**2 + y**2)

    if dist > 10:
        return 0
    elif dist > 5:
        return 1
    elif dist > 1:
        return 5
    else:
        return 10

def main():
    coordX = int(input("Coordinata X: "))

    coordY = int(input("Coordinata Y: "))

    print("Punteggio: ",score(coordX,coordY))

    
if __name__=="__main__":
    main()