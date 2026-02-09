import bisect

def main():
    import sys
    input = sys.stdin.read().split()
    N = int(input[0])
    a = list(map(int, input[1:N+1]))

    prefix = [0] * (N + 1)
    for i in range(1, N+1):
        prefix[i] = prefix[i-1] + a[i-1]

    for i in range(1, N+1):
        # Compute T: subarrays not including i
        left_T = []
        if i > 1:
            left_T = [prefix[e] - prefix[s-1] for s in range(1, i) for e in range(s, i)]
        
        right_T = []
        if i < N:
            ri