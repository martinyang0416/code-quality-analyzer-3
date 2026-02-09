from bisect import bisect_left, bisect_right
from collections import defaultdict

s = input().strip()
counts = defaultdict(int)
for c in s:
    counts[c] += 1

sum_even = sum((v // 2) * 2 for v in counts.values())
any_odd = any(v % 2 != 0 for v in counts.values())
max_len = sum_even + (1 if any_odd else 0)

if max_len >= 100:
    candidate = None
    for c in counts:
        if counts[c] >= 100:
            candidate = c
            break
    if candidate is not None:
        res = []
        cn