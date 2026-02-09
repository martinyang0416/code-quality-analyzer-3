n, k = map(int, input().split())
a = list(map(int, input().split()))
total = 0
for ai in a:
    t = min(3, ai // k)
    total += ai - t * k
print(total)