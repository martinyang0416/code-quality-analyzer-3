import sys
from collections import deque

def compute_diameter(adj):
    def bfs(start):
        visited = [False] * (len(adj) + 1)
        q = deque()
        q.append((start, 0))
        visited[start] = True
        max_dist = 0
        far_node = start
        while q:
            node, dist = q.popleft()
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    new_dist = dist + 1
                    if 