import math

def minimal_additional_matches():
    n = int(input())
    for _ in range(n):
        w, t, a, b = map(int, input().split())
        if a == 0:
            if w == 0:
                print(0)
            else:
                print(-1)
            continue
        
        g = math.gcd(a, b)
        a_prime = a // g
        b_prime = b // g
        
        if a_prime > b_prime:
            print(-1)
            continue
        
        if a_prime == b_prime:
            if w == t: