import sys
from sys import stdin
from collections import deque

def main():
    n, m = map(int, stdin.readline().split())
    forbidden = [set() for _ in range(n+1)]
    for _ in range(m):
        x, y = map(int, stdin.readline().split())
        forbidden[x].add(y)
        forbidden[y].add(x)
    
    remaining = set(range(1, n+1))
    components = []
    
    while remaining:
        u = remaining.pop()
        component = 1
        queue = deque([u])
        while queue:
            current =