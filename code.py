n, x, y = map(int, input().split())
required = (y * n + 99) // 100
clones = max(required - x, 0)
print(clones)