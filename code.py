n, m, k = map(int, input().split())
islands = []
for _ in range(n):
    name = input().strip()
    artifacts = []
    for _ in range(m):
        buy, sell, stock = map(int, input().split())
        artifacts.append((buy, sell, stock))
    islands.append(artifacts)

max_profit = 0

for from_island in range(n):
    for to_island in range(n):
        if from_island == to_island:
            continue
        items = []
        for artifact in range(m):
            a_buy = islands[from_island][artifa