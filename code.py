A, B, C, X, Y = map(int, input().split())
max_k = 2 * max(X, Y)
min_cost = float('inf')

for k in range(0, max_k + 1):
    a = max(0, (2 * X - k + 1) // 2)
    b = max(0, (2 * Y - k + 1) // 2)
    cost = a * A + b * B + k * C
    if cost < min_cost:
        min_cost = cost

print(min_cost)