def main():
    import sys
    data = list(map(int, sys.stdin.readline().split()))
    ptr = 0
    N = data[ptr]
    ptr += 1
    k = data[ptr]
    ptr += 1
    V = data[ptr:ptr+N]
    ptr += N
    B = data[ptr:ptr+N]
    
    dp = {tuple(): 0}
    for i in range(N):
        b = B[i]
        v = V[i]
        new_dp = {}
        for stack in dp:
            current_sum = dp[stack]
            # Option 1: do not take
            if stack in new_dp:
                if current_sum > new_dp[stack]:
 