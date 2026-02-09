def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    N = int(input[idx])
    idx += 1
    F = int(input[idx])
    idx += 1
    V = int(input[idx])
    idx += 1
    pos = []
    for _ in range(N):
        pos.append(int(input[idx]))
        idx += 1
    pos.sort()
    
    if N == 0:
        print(0)
        return

    dp = [float('inf')] * (N + 1)
    dp[0] = 0
    for i in range(1, N + 1):
        for j in range(i):
            cost = F + (pos[i-1] - pos[j]) * V
    