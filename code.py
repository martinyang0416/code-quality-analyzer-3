n, q = map(int, input().split())

lower = [0] * (n + 1)
upper = [0] * (n + 1)

for i in range(1, n + 1):
    lower[i] = 1
    upper[i] = n

for _ in range(q):
    t, l, r, v = map(int, input().split())
    if t == 1:
        for x in range(l, r + 1):
            if lower[x] < v:
                lower[x] = v
    else:
        for x in range(l, r + 1):
            if upper[x] > v:
                upper[x] = v

valid = True
total = 0
for x in range(1, n + 1):
    if lower[x] > upper[x]:
        val