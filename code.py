import math

def kthFactor(n: int, k: int) -> int:
    lower = []
    higher = []
    for i in range(1, math.isqrt(n) + 1):
        if n % i == 0:
            lower.append(i)
            j = n // i
            if j != i:
                higher.append(j)
    factors = lower + higher[::-1]
    return factors[k-1] if len(factors) >= k else -1