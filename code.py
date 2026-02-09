MOD = 10**9 + 7

def main():
    import sys
    N, M = map(int, sys.stdin.readline().split())
    test_solvers = []
    for _ in range(M):
        s = sys.stdin.readline().strip()
        test_solvers.append(s)
    
    max_mask = 1 << M
    count = [0] * max_mask  # Initialize count array for all possible bitmasks
    
    for p in range(N):
        mask = 0
        for m in range(M):
            if test_solvers[m][p] == 'H':
                mask |= 1 << m
        count[mask] += 1
    
    max_