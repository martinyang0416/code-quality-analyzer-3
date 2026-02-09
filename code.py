MOD = 10**9 + 7

def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    N = int(input[idx])
    idx += 1
    M = int(input[idx])
    idx += 1

    edges = []
    for _ in range(M):
        a = int(input[idx]) - 1  # converting to 0-based index
        idx += 1
        b = int(input[idx]) - 1
        idx += 1
        c = int(input[idx])
        idx += 1
        edges.append((c, a, b))

    # Sort edges by cost
    edges.sort()

    # Group edges by cost
    groups = []
  