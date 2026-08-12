def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0   # 0 coins needed to make amount 0

    for a in range(1, amount + 1):
        for coin in coins:
            if coin <= a:
                dp[a] = min(dp[a], dp[a - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1


print(coin_change([1, 2, 5], 11))   # 3 -> 5+5+1
print(coin_change([2], 3))           # -1 -> impossible
