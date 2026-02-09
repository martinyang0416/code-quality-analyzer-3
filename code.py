import bisect

def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    N = int(input[idx]); idx +=1
    a = list(map(int, input[idx:idx+N]))
    idx +=N
    Q = int(input[idx]); idx +=1
    queries = []
    for _ in range(Q):
        i = int(input[idx])-1  # convert to 0-based
        j = int(input[idx+1])
        queries.append( (i, j) )
        idx +=2

    # Preprocessing
    # Create sorted array S in non-decreasing order
    sorted_with_indices = sorted( (a[i], i) fo