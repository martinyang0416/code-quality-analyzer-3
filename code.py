n = int(input())
a = [int(input()) for _ in range(n)]

# Initialize DP table
dp = [[0] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = a[i]

for length in range(2, n + 1):
    for i in range(n - length + 1):
        j = i + length - 1
        max_val = 0
        for k in range(i, j):
            left = dp[i][k]
            right = dp[k+1][j]
            if left == right:
                current = left + 1
            else:
                current = max(left, right)
            if curre