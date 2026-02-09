import sys

def comb(n, k):
    if n < k or k < 0:
        return 0
    if k == 0:
        return 1
    numerator = 1
    for i in range(k):
        numerator *= (n - i)
    denominator = 1
    for i in range(1, k + 1):
        denominator *= i
    return numerator // denominator

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    n = int(line)
    if n == 0:
        break
    if n < 16:
        print(0)
        continue
    if n % 2 == 0:
        m = n // 2
   