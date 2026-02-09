import sys
import heapq

def main():
    n, m, t = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        edges.append((a, b, c))
    d = int(sys.stdin.readline())

    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    for a, b, c in edges:
        adj[a].append((b, c))
        adj[b].append((a, c))

    # Dijkstra's algorithm to find shortest paths from t
    INF = float('inf')
    dist = [INF] 