n = int(input())
degrees = [0] * (n + 1)
for _ in range(n - 1):
    u, v = map(int, input().split())
    degrees[u] += 1
    degrees[v] += 1

s = 0
for i in range(1, n + 1):
    d = degrees[i]
    s += d * (d - 1) // 2

total = (n - 1) + s
print(total)