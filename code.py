import sys
MOD = 10**9 + 7

def main():
    N, M = map(int, sys.stdin.readline().split())
    mask = []
    for _ in range(N):
        s = sys.stdin.readline().strip()
        m = 0
        for c in s:
            m <<= 1
            if c == 'H':
                m |= 1
        mask.append(m)
    
    # Fenwick Tree for 2^M bits (M up to 20 -> 1e6)
    size = 1 << M
    fenwick = [0] * (size + 2)  # 1-based indexing
    
    def update(pos, delta):
        while pos <= size:
            fenwick[p