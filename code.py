def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [0] * n
    dp[0] = arr[0]
    for i in range(1, n):
        max_val = 0
        current_max = -float('inf')
        max_l = min(k, i + 1)
        for l in range(1, max_l + 1):
            start = i - l + 1
            current_max = max(current_max, arr[start])
            prev = dp[start - 1] if start > 0 else 0
            current_sum = prev + current_max * l
            if current_sum > max_val:
                max_val = current_s