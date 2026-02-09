import sys

a, b = map(int, sys.stdin.readline().split())

if a == 0:
    print(-b * b)
    print('x' * b)
    sys.exit(0)
if b == 0:
    print(a * a)
    print('o' * a)
    sys.exit(0)

max_k = min(a, b - 1)
best_score = -float('inf')
best_k = 1

for k in range(1, max_k + 1):
    m = k + 1
    qo, ro = divmod(a, k)
    sum_os = ro * (qo + 1) ** 2 + (k - ro) * qo ** 2
    qx, rx = divmod(b, m)
    sum_xs = rx * (qx + 1) ** 2 + (m - rx) * qx ** 2
    current = sum_os - sum_xs
    if current > bes