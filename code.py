def minimal_games():
    import sys
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    index = 1
    for _ in range(t):
        w = int(data[index])
        l = int(data[index+1])
        p = int(data[index+2])
        q = int(data[index+3])
        index +=4
        
        if p == q:
            # Desired rate is 1
            if l == 0:
                print(0)
            else:
                print(-1)
            continue
        if p == 0:
            if q != 