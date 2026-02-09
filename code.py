import bisect

def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    N = int(input[idx])
    idx += 1
    Q = int(input[idx])
    idx += 1

    s = input[idx]
    idx += 1
    spec_str = input[idx]
    idx += 1

    # Parse L and R positions
    L = []
    R = []
    for pos, c in enumerate(s):
        if c == 'L':
            L.append(pos)
        else:
            R.append(pos)
    assert len(L) == N and len(R) == N

    # Precompute next_furthest for each tractor (1-