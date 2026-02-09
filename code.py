T = int(input())
for _ in range(T):
    K = int(input())
    for i in range(1, K+1):
        start = (i-1) * K + 1
        line = ''.join(str(start + j) for j in range(K))
        print(line)