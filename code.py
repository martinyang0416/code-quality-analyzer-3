import sys
from collections import deque

def rotate_right(s, N):
    # Rotate the bit pattern of 's' right by 1, where 's' is an integer
    last_bit = s & 1
    s = (s >> 1) | (last_bit << (N - 1))
    return s

def main():
    input = sys.stdin.read().split()
    T = int(input[0])
    N = int(input[1])
    index = 2
    cases = []
    for _ in range(T):
        lights_str = input[index]
        switches_str = input[index + 1]
        index += 2
        # Convert to integers (LSB is first char