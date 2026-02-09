def findTargetSumWays(nums, S):
    total = sum(nums)
    if (total + S) % 2 != 0 or (total + S) < 0:
        return 0
    P = (total + S) // 2
    dp = [0] * (P + 1)
    dp[0] = 1
    for num in nums:
        for i in range(P, num - 1, -1):
            dp[i] += dp[i - num]
    return dp[P]