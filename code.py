MOD = 10**9 + 7

def compute(s):
    from math import factorial
    from collections import Counter
    
    counts = Counter(s)
    a = counts.get('A', 0)
    b = counts.get('B', 0)
    n = a + b
    
    numerator = factorial(n)
    denominator = factorial(a) * factorial(b)
    
    result = (numerator // denominator) % MOD
    return result

# Read input
s = input().strip()

# Compute and print the result
print(compute(s))