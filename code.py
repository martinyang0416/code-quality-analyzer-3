import bisect
import sys

def main():
    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr])
    ptr += 1
    for _ in range(T):
        N, Q = map(int, input[ptr:ptr+2])
        ptr += 2
        A = list(map(int, input[ptr:ptr+N]))
        ptr += N
        sorted_A = sorted(A)
        element_to_pos = {val: i+1 for i, val in enumerate(A)}  # 1-based
        
        # Precompute sorted list for S_l and S_g
        sorted_values = sorted_A
        
        for __ in range(Q):
 