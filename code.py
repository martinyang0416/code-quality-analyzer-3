def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    M = int(input[idx])
    idx += 1
    D = int(input[idx])
    idx += 1
    
    stations = []
    for _ in range(M):
        f = int(input[idx])
        p = int(input[idx + 1])
        stations.append((p, f))
        idx += 2
    
    stations.sort()  # Sort by position
    left = 0
    current_sum = 0
    max_sum = 0
    
    for right in range(len(stations)):
        current_sum += stations[right][1]
        while s