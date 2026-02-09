def main():
    import sys
    N, K, T = map(int, sys.stdin.readline().split())
    initial_active = list(map(int, sys.stdin.readline().split()))
    
    effective_T = T % N
    
    # Initialize the positions array
    pos = list(range(N))
    
    # The initial current_cows is the cows at the initial active positions
    current_cows = [pos[A] for A in initial_active]
    
    for step in range(1, effective_T + 1):
        # Rotate the current_cows: [a0, a1, ..., aK-1] becomes [aK-1, a0, a1, 