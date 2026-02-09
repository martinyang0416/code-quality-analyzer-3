import math

def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    n = int(input[idx])
    idx += 1
    m = int(input[idx])
    idx += 1
    
    a = list(map(int, input[idx:idx+n]))
    idx += n
    b = list(map(int, input[idx:idx+m]))
    idx += m
    x = int(input[idx])
    idx += 1

    # Precompute log of x
    log_x = math.log(x)

    # Precompute for a: minimal log sum for each possible subarray length
    min_log_a = {}
    for s in range(1, n+1):
        min_lo