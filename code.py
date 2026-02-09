def stoneGameIII(stoneValue):
    n = len(stoneValue)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + stoneValue[i]
    
    dp = [0] * (n + 4)  # Extra space to handle i+3 up to n
    
    for i in reversed(range(n)):
        dp[i] = -float('inf')
        for k in range(1, 4):
            if i + k > n:
                continue
            current_sum = prefix[i + k] - prefix[i]
            dp[i] = max(dp[i], current_sum - dp[i + k])
    
    result = dp[0]
