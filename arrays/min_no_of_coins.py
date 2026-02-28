def min_coins(V):
    coins = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    result = []
    for coin in coins:
        if V >= coin:
            count = V // coin  
            V -= count * coin  
            result.extend([coin] * count)
    return result
amount = 93
ans = min_coins(amount)
print("Coins used:", ans)
print("Minimum coins required:", len(ans))