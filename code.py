import sys

max_n = 10**6

# Precompute smallest prime factors (SPF)
spf = list(range(max_n + 1))
for i in range(2, int(max_n**0.5) + 1):
    if spf[i] == i:
        for j in range(i*i, max_n + 1, i):
            if spf[j] == j:
                spf[j] = i

# Precompute results for all possible n
precomputed = [""] * (max_n + 1)
for n in range(2, max_n + 1):
    factors = {}
    temp = n
    while temp > 1:
        p = spf[temp]
        while temp % p == 0:
            factors[p] = factors.get(p,