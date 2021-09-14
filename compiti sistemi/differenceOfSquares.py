def differenceOfSquares(rangeNum):

    squareSum = 0
    sumSquare = 0
    
    for k in range(1, rangeNum + 1):
        squareSum += k
    squareSum = squareSum**2
    
    for k in range(1, rangeNum + 1):
        sumSquare += k**2
    
    return squareSum, sumSquare, squareSum - sumSquare

print(differenceOfSquares(10))