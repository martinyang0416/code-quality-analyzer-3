import sys

def solve():
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    for _ in range(T):
        n = int(input[idx])
        k = int(input[idx + 1])
        idx += 2
        s = input[idx]
        idx += 1
        if n % k != 0:
            print(-1)
            continue
        # Precompute prefix counts
        prefix_counts = [[0] * 26 for _ in range(n + 1)]
        for i in range(n):
            for ch in range(26):
                prefix_counts[i