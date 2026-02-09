def coinChange(coins, amount):
    if amount == 0:
        return 0
    max_val = amount + 1
    dp = [max_val] * (max_val)
    dp[0] = 0
    for i in range(1, max_val):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] <= amount else -1