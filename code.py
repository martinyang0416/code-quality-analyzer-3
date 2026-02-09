import math

def get_divisors(n):
    divisors = set()
    for i in range(1, int(math.isqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return divisors

def main():
    import sys
    input = sys.stdin.read().split()
    N = int(input[0])
    a = list(map(int, input[1:N+1]))
    a_sorted = sorted(a)
    
    divisors = set()
    for num in a_sorted:
        divisors.update(get_divisors(num))
    
    # Add values around the first element
    