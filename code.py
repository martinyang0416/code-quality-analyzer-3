def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx]); idx += 1

    # Precompute all possible pairings of the numbers 1-6 into three pairs
    all_pairings = []
    elements = [1, 2, 3, 4, 5, 6]
    def backtrack(remaining, current_pairs):
        if not remaining:
            all_pairings.append(current_pairs)
            return
        first = remaining[0]
        for i in range(1, len(remaining)):
            pair = (first, remaining[i])
        