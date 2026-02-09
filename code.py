a1, a2, a3 = map(int, input().split())
prev, curr = a1, a2
for _ in range(a3 - 1):
    next_t = prev + curr
    prev, curr = curr, next_t
print(curr)