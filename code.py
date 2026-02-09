def winnerSquareGame(n):
    max_square_root = int(n ** 0.5)
    squares = [i*i for i in range(max_square_root, 0, -1)]
    dp = [False] * (n + 1)
    dp[0] = False
    for i in range(1, n + 1):
        for s in squares:
            if s > i:
                continue
            if not dp[i - s]:
                dp[i] = True
                break
    return dp[n]