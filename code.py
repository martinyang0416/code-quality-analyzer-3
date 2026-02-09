def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    N = int(input[idx])
    idx +=1
    if N == 0:
        print(0)
        return
    points = []
    for _ in range(N):
        x = int(input[idx])
        y = int(input[idx+1])
        points.append((x, y))
        idx +=2
    
    if N ==1:
        print(0)
        return
    
    # Compute distance matrix
    dist = [[0]*N for _ in range(N)]
    for i in range(N):
        x1, y1 = points[i]
        for j in range(N)