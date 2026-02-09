import heapq

def main():
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    s = int(input())
    
    INF = float('inf')
    distance = [INF] * n
    distance[s] = 0
    heap = [(0, s)]
    
    while heap:
        current_dist, u = heapq.heappop(heap)
        if current_dist > distance[u]:
            continue
        for v, w in adj[u]:
        