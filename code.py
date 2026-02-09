import sys

def main():
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    for _ in range(T):
        K = int(input[idx])
        N = int(input[idx + 1])
        idx += 2
        
        # Compute mod8 part
        T8 = 8
        m8, r8 = divmod(K, T8)
        sum_p8 = sum(pow(i, N, 8) for i in range(1, T8 + 1))
        sum_r8 = sum(pow(i, N, 8) for i in range(1, r8 + 1))
        mod8 = (m8 * sum_p8 + sum_r8) % 8
        
        # Compute mod125 part
    