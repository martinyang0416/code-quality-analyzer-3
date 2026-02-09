n, s = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
k = n // 2
cost = 0

# Adjust elements up to the median to be <= s
for i in range(k + 1):
    if a[i] > s:
        cost += a[i] - s

# Adjust elements from the median onwards to be >= s
for i in range(k, n):
    if a[i] < s:
        cost += s - a[i]

print(cost)