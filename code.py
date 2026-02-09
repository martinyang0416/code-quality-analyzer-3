import sys

def main():
    input = sys.stdin.read().split()
    ptr = 0
    N, Q = int(input[ptr]), int(input[ptr+1])
    ptr +=2
    A = list(map(int, input[ptr:ptr+N]))
    ptr += N
    # Using 1-based indexing
    A = [0] + A  # A[1..N]
    next = [0]*(N+2)  # next[1..N]

    # Precompute next array
    for i in range(1, N+1):
        next[i] = i
        max_j = min(i + 100, N)
        for j in range(i+1, max_j +1):
            if A[j] > A[i]:
                next[i] = j
                brea