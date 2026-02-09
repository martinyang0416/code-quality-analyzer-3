from collections import deque
import sys

def main():
    r, c = map(int, sys.stdin.readline().split())
    grid = []
    for _ in range(r):
        row = list(sys.stdin.readline().strip())
        grid.append(row)
    
    visited = [[False for _ in range(c)] for _ in range(r)]
    count = 0
    
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 'L' and not visited[i][j]:
                # BFS to mark all connected land cells
                queue = deque()
        