import sys

def main():
    sys.setrecursionlimit(1 << 25)
    N = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    
    prefix = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix[i] = prefix[i - 1] + a[i - 1]
    
    subarrays = []
    for l in range(1, N + 1):
        for r in range(l, N + 1):
            s = prefix[r] - prefix[l - 1]
            subarrays.append((l, r, s))
    
    S = [s for (l, r, s) in subarrays]
    
    for i in range(1, N + 1)