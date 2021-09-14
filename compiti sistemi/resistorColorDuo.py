colorValue = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9
}

def resistorColorDuo(x, y):
    x = x.lower()
    y = y.lower()
    
    if x in colorValue and y in colorValue:
        value = str(colorValue[x]) + str(colorValue[y])
    else:
        return "Wrong input"

    return (value)

print(resistorColorDuo("green", "red"))