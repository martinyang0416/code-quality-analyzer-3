def minimal_cost():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    idx = 1
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        c = list(map(int, data[idx:idx+n]))
        idx += n
        
        prefix = [0] * (n + 1)
        for i in range(1, n+1):
            prefix[i] = prefix[i-1] + c[i-1]
        
        if n == 0:
            print(0)
            continue
        
        right_dp = [0] * (n + 1)
        min_righ