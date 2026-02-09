import bisect

def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    N, Q = int(input[idx]), int(input[idx+1])
    idx +=2
    s = input[idx]
    idx +=1
    spec = input[idx]
    idx +=1

    # Parse L and R into positions
    L = []
    R = []
    ptr = 0
    for c in s:
        if c == 'L':
            L.append(ptr)
            ptr +=1
        else:
            R.append(ptr)
            ptr +=1
    # The intervals are given as L and R in the string, which are in orde