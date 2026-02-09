import sys
from collections import deque

def main():
    n = int(sys.stdin.readline())
    edges = []
    for _ in range(n-1):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
    
    # Build adjacency list
    adj = [[] for _ in range(n+1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Find connected components using BFS
    visited = [False] * (n + 1)
    components = []
    for i in range(1, n + 1):
        if not visit