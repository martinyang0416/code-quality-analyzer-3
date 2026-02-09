import sys
from collections import deque

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        B = list(map(int, data[idx:idx+N]))
        idx += N
        D = [B[i] - A[i] for i in range(N)]
        edges = [[] for _ in range(N)]
        for _ in range(N-1):
            u = int(data[idx]) - 1  # conve