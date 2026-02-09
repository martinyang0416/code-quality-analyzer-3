import math

def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    sqrt_n = int(math.sqrt(n)) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False
    return True

t = int(input())
for _ in range(t):
    num = int(input())
    if is_prime(num):
        print("PRIME")
    else:
        print("NOT PRIME")