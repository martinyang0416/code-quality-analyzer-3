def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    N, K = int(input[idx]), int(input[idx+1])
    idx += 2
    
    cuboids = []
    x_coords = set()
    y_coords = set()
    z_coords = set()
    
    for _ in range(N):
        x1 = int(input[idx])
        y1 = int(input[idx+1])
        z1 = int(input[idx+2])
        x2 = int(input[idx+3])
        y2 = int(input[idx+4])
        z2 = int(input[idx+5])
        idx += 6
        
        cuboids.append( (x1, y1, z1, x2, y