import heapq

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    N = int(data[idx])
    Q = int(data[idx+1])
    idx += 2
    roadworks = []
    for _ in range(N):
        S = int(data[idx])
        T = int(data[idx+1])
        X = int(data[idx+2])
        idx +=3
        lower = S - X - 0.5
        upper = T - X - 0.5
        roadworks.append( (lower, upper, X) )
    roadworks.sort()
    ds = list(map(int, data[idx:idx+Q]))
    heap = []
    j = 0
 