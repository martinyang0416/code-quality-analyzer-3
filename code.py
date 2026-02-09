h, w = map(int, input().split())
grid = [input().strip() for _ in range(h)]

# Initialize horizontal and vertical matrices
horizontal = [[0 for _ in range(w)] for __ in range(h)]
vertical = [[0 for _ in range(w)] for __ in range(h)]

for i in range(h):
    for j in range(w):
        # Check for horizontal pairs
        if j < w - 1 and grid[i][j] == '.' and grid[i][j+1] == '.':
            horizontal[i][j] = 1
        else:
            horizontal[i][j] = 0
        # Check for vertical pairs
    