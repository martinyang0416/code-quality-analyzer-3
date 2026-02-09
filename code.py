import sys
import math

def sieve(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.isqrt(n)) + 1):
        if sieve[i]:
            sieve[i*i::i] = [False] * len(sieve[i*i::i])
    primes = [i for i, is_p in enumerate(sieve) if is_p]
    return primes

base_primes = sieve(31623)

t = int(sys.stdin.readline())
for case in range(t):
    m, n = map(int, sys.stdin.readline().split())
    size = n - m + 1
    is_prime = [True] * size
    
    for i in ra