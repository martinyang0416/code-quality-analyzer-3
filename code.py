def factorize(m):
    factors = {}
    i = 2
    while i * i <= m:
        while m % i == 0:
            factors[i] = factors.get(i, 0) + 1
            m //= i
        i += 1
    if m > 1:
        factors[m] = 1
    return factors

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    m = int(data[1])
    a = list(map(int, data[2:2+n]))
    
    factors = factorize(m)
    if not factors:
        print("YES")
        return
    
    primes = li