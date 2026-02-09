import heapq
import sys

def main():
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx +=1
    for _ in range(T):
        N = int(input[idx])
        idx +=1
        left = []
        right = []
        for __ in range(N):
            K = int(input[idx])
            L = int(input[idx+1])
            R = int(input[idx+2])
            idx +=3
            if L >= R:
                left.append( (K, L, R) )
            else:
                right.append( (K, L, R) )
  