def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    q = int(data[1])
    a = list(map(int, data[2:n + 2]))
    diff = [0] * (n + 2)
    
    index = n + 2
    for i in range(q):
        l = int(data[index])
        r = int(data[index + 1])
        index += 2
        diff[l] += 1
        if r + 1 <= n:
            diff[r + 1] -= 1
    
    weights = []
    current = 0
    for i in range(1, n + 1):
        current += diff[i]
        weight