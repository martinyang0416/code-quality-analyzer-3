def maxProductPath(grid):
    MOD = 10**9 + 7
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    dp = [[(0, 0) for _ in range(cols)] for _ in range(rows)]
    dp[0][0] = (grid[0][0], grid[0][0])
    
    for i in range(rows):
        for j in range(cols):
            if i == 0 and j == 0:
                continue
            candidates = []
            if i > 0:
                up_max, up_min = dp[i-1][j]
                candidates.append(up_max * grid[i][j])
                candida