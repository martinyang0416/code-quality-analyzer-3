import sys
from sys import stdin
from collections import deque

def main():
    sys.setrecursionlimit(1 << 25)
    N = int(stdin.readline())
    s = stdin.readline().strip()
    adj = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a, b = map(int, stdin.readline().split())
        adj[a].append(b)
        adj[b].append(a)
    
    cow_nodes = [i for i in range(1, N+1) if s[i-1] == '1']
    total_cow = len(cow_nodes)
    if total_cow == 0:
        print(0)  # Problem states there is at 