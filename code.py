import sys

def main():
    s = list(sys.stdin.readline().strip())
    N = len(s)
    U = int(sys.stdin.readline())
    updates = []
    for _ in range(U):
        p, c = sys.stdin.readline().split()
        p = int(p) - 1  # convert to 0-based
        updates.append((p, c))

    T = ['b', 'e', 's', 's', 'i', 'e']
    # Precompute the initial D array
    D = []
    prev_dp = [1, 0, 0, 0, 0, 0, 0]  # initial state before first character
    for i in range(N):
        current_char = s[i]
        n