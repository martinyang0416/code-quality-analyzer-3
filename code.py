from collections import deque
import sys

def main():
    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr])
    ptr += 1
    for _ in range(T):
        N = int(input[ptr])
        M = int(input[ptr+1])
        ptr +=2
        adj = [[] for _ in range(N+1)]
        for __ in range(M):
            X = int(input[ptr])
            Y = int(input[ptr+1])
            adj[X].append(Y)
            adj[Y].append(X)
            ptr +=2
        distance = [-1]*(N+1)
        distance[1] = 