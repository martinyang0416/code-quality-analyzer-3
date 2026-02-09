def main():
    import sys
    S, T, q = sys.stdin.readline().split()
    q = int(q)
    n = len(S)
    m = len(T)
    
    # Precompute the merged strings' comparison keys
    # But we can't store all merged strings; compare on the fly
    
    for _ in range(q):
        l, r, k, x, y = map(int, sys.stdin.readline().split())
        candidates = []
        # Generate all i in [l, r] where i mod k is in [x, y]
        # This can be optimized by finding the first i >= l with i mod k = c, then ste