def is_lucky(s):
    return all(c in {'0', '4', '7'} for c in s)

def solve():
    import sys
    input = sys.stdin.read().split()
    t = int(input[0])
    cases = input[1:t+1]

    # Precompute possible sums for 6 digits of 0,4,7
    max_sum = 6*7
    possible = [False] * (max_sum + 1)
    # Generate all possible sums with exactly 6 digits
    from itertools import product
    for digits in product([0,4,7], repeat=6):
        s = sum(digits)
        possible[s] = True

    for n_str in cases:
