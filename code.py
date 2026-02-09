t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    max_ops = 0
    x_max = min(a, b // 2)
    for x in range(x_max + 1):
        current_b = b - 2 * x
        y = min(current_b, c // 2)
        max_ops = max(max_ops, x + y)
    print(max_ops * 3)