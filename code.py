import bisect
import math
from collections import defaultdict

def reverse_num(x):
    return int(str(x)[::-1].lstrip('0') or '0')

maxx, maxy, w = map(int, input().split())

# Preprocess a_ratios and b_ratios
a_ratios = defaultdict(list)
for a in range(1, maxx + 1):
    rev_a = reverse_num(a)
    d = math.gcd(a, rev_a)
    p = a // d
    q = rev_a // d
    a_ratios[(p, q)].append(a)

for key in a_ratios:
    a_ratios[key].sort()

b_ratios = defaultdict(list)
for b in range(1, maxy + 1):
    rev