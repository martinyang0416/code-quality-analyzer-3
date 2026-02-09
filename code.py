n, x = map(int, input().split())
k = int(input())
c = 0
for _ in range(k):
    t, _ = map(int, input().split())
    if t == 1:
        c += 1

u = (x - 1) - k
min_skipped = 0
max_skipped = u

print(min_skipped, max_skipped)