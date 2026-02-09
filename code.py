import bisect

def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    N = int(input[idx])
    idx += 1
    Q = int(input[idx])
    idx += 1

    S = input[idx]
    idx += 1
    special_str = input[idx]
    idx += 1

    # Parse L and R positions
    Ls = []
    Rs = []
    for i in range(len(S)):
        c = S[i]
        pos = i + 1  # 1-based positions
        if c == 'L':
            Ls.append(pos)
        else:
            Rs.append(pos)
    
    # Special array (1-ba