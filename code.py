import sys
from collections import defaultdict

def main():
    for line in sys.stdin:
        X_Y_Z = line.strip().split()
        if X_Y_Z == ['0', '0', '0']:
            break
        X, Y, Z = map(int, X_Y_Z)
        V = list(map(int, sys.stdin.readline().split()))
        event_map = {}
        for _ in range(Z):
            Ni, Ei, Ai = map(int, sys.stdin.readline().split())
            event_map[Ni] = (Ei, Ai)
        
        dp = [defaultdict(float) for _ in range(Y)]
        dp[0][0] =