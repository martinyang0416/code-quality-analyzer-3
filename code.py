s = int(input())
for _ in range(s):
    original = input().strip()
    received = input().strip()
    A = original.lower()
    B = received.lower()
    m = len(A)
    n = len(B)
    
    # Initialize DP table
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][0] = i
    for j in range(1, m + 1):
        dp[0][j] = float('inf')
    
    # Fill DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            sub_cost = 0 if B[i-1] == A[j-