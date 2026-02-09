n = int(input())

if n == 1:
    print(2)
else:
    primes = [2]
    candidate = 3
    while len(primes) < n:
        is_prime = True
        sqrt_m = int(candidate ** 0.5) + 1
        for p in primes:
            if p > sqrt_m:
                break
            if candidate % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
        candidate += 2
    print(primes[-1])