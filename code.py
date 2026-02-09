# Read the grid
grid = []
for _ in range(3):
    row = list(map(int, input().split()))
    grid.append(row)

# Calculate the sum of all elements (including zeros)
sum_known = sum(num for row in grid for num in row)

# Determine the magic sum S
S = sum_known // 2

# Compute the missing diagonal elements
x = S - grid[0][1] - grid[0][2]
y = S - grid[1][0] - grid[1][2]
z = S - grid[2][0] - grid[2][1]

# Update the grid with computed values
grid[0][0] = x
grid[1][1] = y
grid[2][2] = z

# Print the re