import bisect

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    k = int(data[idx+1])
    q = int(data[idx+2])
    idx +=3
    
    MAX = 200000
    diff = [0] * (MAX + 2)  # 0 to MAX+1
    
    for _ in range(n):
        l = int(data[idx])
        r = int(data[idx+1])
        idx +=2
        diff[l] += 1
        if r + 1 <= MAX:
            diff[r + 1] -= 1
    
    current = 0
    freq = [0] * (MAX + 1)  # 1 to MAX
    