import bisect
from collections import defaultdict

n, m, y0, y1 = map(int, input().split())
mice = list(map(int, input().split()))
cheeses = list(map(int, input().split()))
mice.sort()
cheeses.sort()

dy = abs(y0 - y1)

if m == 0:
    print(n)
    exit()

unique = [[] for _ in range(m)]
tie_groups = defaultdict(list)

for x in mice:
    j = bisect.bisect_left(cheeses, x)
    candidates = []
    if j > 0:
        candidates.append(j-1)
    if j < m:
        candidates.append(j)
    min_dist_sq = 