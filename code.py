import sys
from collections import deque

def rotate_right(s, N):
    lsb = s & 1
    s = s >> 1
    s |= (lsb << (N - 1))
    return s & ((1 << N) - 1)  # Ensure it stays within N bits

def main():
    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr])
    ptr += 1
    N = int(input[ptr])
    ptr += 1

    for _ in range(T):
        light = input[ptr]
        switch = input[ptr + 1]
        ptr += 2

        L0 = int(light, 2)
        S0 = int(switch, 2)
        target = L0

 