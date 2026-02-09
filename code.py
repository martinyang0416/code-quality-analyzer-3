import sys

def is_grid_stable(R, C, grid):
    for i in range(R):
        for j in range(C):
            neighbors = 4
            if i == 0 or i == R - 1:
                neighbors -= 1
            if j == 0 or j == C - 1:
                neighbors -= 1
            if neighbors <= grid[i][j]:
                return False
    return True

def main():
    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr])
    ptr += 1
    for _ in range(T):
        R = int(input[ptr])
        C