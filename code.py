import sys
from collections import deque

def main():
    sys.setrecursionlimit(1 << 25)
    N, M = map(int, sys.stdin.readline().split())
    values = [0] * (N + 1)  # 1-based indexing
    for i in range(1, N+1):
        values[i] = int(sys.stdin.readline())
    adj = [[] for _ in range(N+1)]
    in_degree = [0] * (N+1)
    for _ in range(M):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        in_degree[v] += 1

    # Compute topological order
    queue = dequ