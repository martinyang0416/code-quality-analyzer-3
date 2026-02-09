import sys

def main():
    s = sys.stdin.readline().strip()
    U = int(sys.stdin.readline())
    updates = []
    for _ in range(U):
        p, c = sys.stdin.readline().split()
        updates.append((int(p) - 1, c))  # Convert to 0-based index

    target = ['b', 'e', 's', 's', 'i', 'e']
    N = len(s)
    s_list = list(s)

    # Precompute initial prev_state and C
    prev_state = [[0] * 6 for _ in range(N + 1)]
    prev_state[0] = [0] * 6
    current = [0] * 6

    for i in range(N):
      