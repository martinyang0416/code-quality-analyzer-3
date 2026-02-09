import sys
from collections import defaultdict

MOD = 10**9

def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        arr = list(map(int, sys.stdin.readline().split()))
        freq = defaultdict(int)
        freq[0] = 1
        current = 0
        count = 0
        for num in arr:
            current = (current + num) % MOD
            count += freq[current]
            freq[current] += 1
        print(count)

if __name__ == "__main__":
