import heapq

n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
important = []
for _ in range(k):
    x, y = map(int, input().split())
    important.append((x-1, y-1))

index_map = {(x, y): i for i, (x, y) in enumerate(important)}

INF = float('inf')
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
full_mask = (1 << k) - 1

# Initialize distance and predecessor arrays
dist = [[[INF] * (1 << k) for _ in range(m)] for __ in range(n)]
prev = [[[None] * (1 << k) fo