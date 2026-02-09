import numpy as np

def main():
    import sys
    N, K, T = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    
    # Compute D array for each initial A_j
    D = [0] * K
    for j in range(K):
        next_j = (j + 1) % K
        D[j] = (A[next_j] - A[j]) % N
    
    # Compute sum_D[s] which is the sum of D[j] where A[j] == s
    sum_D = [0] * N
    for j in range(K):
        s = A[j]
        sum_D[s] += D[j]
    
    # Compute count array for each