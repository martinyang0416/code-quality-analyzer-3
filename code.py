def countServers(grid):
    if not grid:
        return 0
    rows = len(grid)
    cols = len(grid[0])
    row_counts = [sum(row) for row in grid]
    col_counts = [sum(col) for col in zip(*grid)]
    count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1 and (row_counts[i] > 1 or col_counts[j] > 1):
                count += 1
    return count