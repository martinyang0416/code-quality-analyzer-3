n, m = map(int, input().split())
scores = list(map(int, input().split()))

excluded = []
for i in range(n):
    if scores[i] < m:
        excluded.append(i + 1)  # 1-based index

excluded.sort()

for idx in excluded:
    print(idx)