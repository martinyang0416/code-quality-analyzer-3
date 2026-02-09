import sys
from collections import deque

def rotate_right(s, N):
    return (s >> 1) | ((s & 1) << (N - 1))

def main():
    T, N = map(int, sys.stdin.readline().split())
    for _ in range(T):
        L_str, S_str = sys.stdin.readline().split()
        L_mask = 0
        for i in range(N):
            if L_str[i] == '1':
                L_mask ^= (1 << (N - 1 - i))
        S_mask = 0
        for i in range(N):
            if S_str[i] == '1':
                S_mask ^= (1 << (N - 1 - i))
       