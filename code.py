a1, a2, n = map(int, input().split())
prev, curr = a1, a2
for _ in range(n - 1):
    next_term = prev + curr
    prev, curr = curr, next_term
print(curr)