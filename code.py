import bisect

def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    N = int(input[idx])
    idx += 1
    a = list(map(int, input[idx:idx+N]))
    idx += N
    original_indices = list(range(N))
    
    # Sort the array along with original indices in descending order of values
    sorted_with_indices = sorted(
        zip(a, original_indices),
        key=lambda x: (-x[0], x[1])
    )
    S = [x[0] for x in sorted_with_indices]
    # Create pos_in_sorted array to track 