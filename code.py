import math

n, px, py = map(int, input().split())

vertices = []
dists = []

for _ in range(n):
    x, y = map(int, input().split())
    dx = x - px
    dy = y - py
    dist = math.hypot(dx, dy)
    vertices.append((x, y))
    dists.append(dist)

min_dist = min(dists)
max_dist = max(dists)

for i in range(n):
    a = vertices[i]
    b = vertices[(i + 1) % n]
    ax, ay = a
    bx, by = b
    dx_edge = bx - ax
    dy_edge = by - ay
    len_ab_sq = dx_edge ** 2 + dy_edge ** 2
    if len_ab_sq == 