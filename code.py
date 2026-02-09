import sys
from collections import deque

def main():
    sys.setrecursionlimit(1 << 25)
    n = int(sys.stdin.readline())
    edges = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u, v = map(int, sys.stdin.readline().split())
        edges[u].append(v)
        edges[v].append(u)
    
    LOG = 20
    up = [[-1]*(n+1) for _ in range(LOG)]
    depth = [0]*(n+1)
    visited = [False]*(n+1)
    q = deque([1])
    visited[1] = True
    up[0][1] = -1
    
    while q:
        u = q.poplef