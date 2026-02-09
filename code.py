import sys
import bisect
from collections import deque

def main():
    sys.setrecursionlimit(1 << 25)
    N = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    adj = [[] for _ in range(N + 1)]  # 1-based indexing

    for _ in range(N - 1):
        a, b = map(int, sys.stdin.readline().split())
        adj[a].append(b)
        adj[b].append(a)

    # Step 1: Find all regions (connected components of required nodes)
    region_id = [-1] * (N + 1)  # nodes are 1-based
    regions 