def change(balance):
    coin = [1, 5, 10, 25, 100]
    balanceChange = []

    while balance != 0:
        if balance >= min(coin):
            if balance >= max(coin):
                balanceChange.append(max(coin))
                balance -= max(coin)
            else:
                coin.remove(max(coin))
        else:
            return False

    return balanceChange

print(change(111))