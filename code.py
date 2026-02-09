import sys

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_d = int(n ** 0.5) + 1
    for i in range(3, max_d, 2):
        if n % i == 0:
            return False
    return True

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    print("WIN" if is_prime(n) else "LOSE")