# Read input values
N, M = map(int, input().split())

# Check if N is less than or equal to M*(M-1)
if N <= M * (M - 1):
    print("YES")
else:
    print("NO")