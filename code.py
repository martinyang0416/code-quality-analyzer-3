import sys

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx+n]))
        idx += n
        if n == 1:
            print("Yes")
            continue
        
        # Compute left_valid and is_left_possible
        left_valid = [False] * n
        for i in range(n):
            left_valid[i] = a[i] >= i
        
        is_left