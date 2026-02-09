import bisect
import sys

def main():
    sys.setrecursionlimit(1 << 25)
    N = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    adj = [[] for _ in range(N+1)]
    for _ in range(N-1):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    ans = [0] * (N + 1)
    tails = []
    stack = []
    change_stack = []
    stack.append((1, None, False))
    while stack:
        u, parent, visited = stack.pop()
       