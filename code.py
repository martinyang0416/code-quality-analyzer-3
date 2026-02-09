def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    N = int(input[ptr])
    ptr += 1
    Q = int(input[ptr])
    ptr += 1

    edges = []
    for _ in range(N - 1):
        u = int(input[ptr])
        ptr += 1
        v = int(input[ptr])
        ptr += 1
        s = int(input[ptr])
        ptr += 1
        edges.append((-s, u, v))  # Use negative to sort in ascending and reverse later

    edges.sort()
    edges = [(-e[0], e[1], e[2]) for e in edges]  # Convert back t