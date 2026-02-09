def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    N = int(input[idx])
    idx += 1
    R = int(input[idx])
    idx += 1

    beds = []
    for _ in range(N):
        f = int(input[idx])
        p = int(input[idx+1])
        beds.append((p, f))
        idx += 2

    # Sort the flower beds by their positions
    beds.sort()

    # Extract positions and flowers
    p = [x[0] for x in beds]
    f = [x[1] for x in beds]

    # Compute prefix sums
    prefix = [0] * (N + 