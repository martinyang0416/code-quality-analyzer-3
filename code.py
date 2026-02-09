import sys
from collections import deque

def main():
    while True:
        line = sys.stdin.readline().strip()
        while line == '':
            line = sys.stdin.readline().strip()
        n, m = map(int, line.split())
        if n == 0 and m == 0:
            break
        grid = []
        target = None
        for i in range(m):
            row = sys.stdin.readline().strip()
            grid.append(row)
            for j in range(n):
                if row[j] == '&':
                  