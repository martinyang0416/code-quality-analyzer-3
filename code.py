n, k = map(int, input().split())
max_s = 0

for _ in range(k):
    parts = list(map(int, input().split()))
    mi = parts[0]
    a = parts[1:]
    if a[0] != 1:
        continue
    current_s = 1
    for i in range(1, mi):
        if a[i] == a[i-1] + 1:
            current_s += 1
        else:
            break
    if current_s > max_s:
        max_s = current_s

ans = 2 * n - k - 2 * max_s + 1
print(ans)