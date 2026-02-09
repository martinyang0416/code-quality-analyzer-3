from collections import defaultdict

# Read input values
N, M, L = map(int, input().split())
S = input().strip()

# Precompute the sum of (start+1) for each substring of length L in S
substring_sums = defaultdict(int)
for i in range(N - L + 1):
    substr = S[i:i+L]
    substring_sums[substr] += (i + 1)

# Calculate the results for each query substring
total_sum = 0
count = 0
for _ in range(M):
    T = input().strip()
    if T in substring_sums:
        total_sum += substring_sums[T]
        cou