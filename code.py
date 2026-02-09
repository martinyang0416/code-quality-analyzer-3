import sys

def main():
    n, m, k = map(int, sys.stdin.readline().split())
    d = list(map(int, sys.stdin.readline().split()))
    
    start_count = 0
    start_node = -1
    max_d = 0
    for i in range(n):
        dist = d[i]
        if dist == 0:
            start_count += 1
            start_node = i + 1
        if dist > max_d:
            max_d = dist
    
    if start_count != 1:
        print(-1)
        return
    
    # Check all distances 1 to max_d exist
    possible = True
    f