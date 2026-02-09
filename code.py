import sys

def solve():
    input = sys.stdin.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        N = int(input[idx])
        Y = int(input[idx+1])
        idx +=2
        
        T_min = N * (N +1) //2
        if Y < T_min or Y > N*N:
            print(-1)
            continue
        
        D = Y - T_min
        
        m = list(range(1, N+1))
        remaining = D
        
        # Backward pass to adjust the maximum array
        for i in range(N-2, -1, -1):