def factorize(k):
    factors = {}
    for i in range(2, int(k**0.5) + 1):
        while k % i == 0:
            factors[i] = factors.get(i, 0) + 1
            k = k // i
    if k > 1:
        factors[k] = 1
    return factors

n, k = map(int, input().split())
b = list(map(int, input().split()))

factors = factorize(k)
primes = list(factors.keys())
required = factors

sum_exponents = {p: 0 for p in primes}

for num in b:
    for p in primes:
        cnt = 0
        temp = num  # Create a tempora