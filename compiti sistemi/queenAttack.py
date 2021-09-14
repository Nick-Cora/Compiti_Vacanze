def queenAttack(xW, yW, xB, yB):
    if xW == xB:
        return True
    elif yW == yB:
        return True
    elif abs(xW-xB) == abs(yW-yB):
        return True
    else:
        return False

print(queenAttack(3, 2, 5, 4))