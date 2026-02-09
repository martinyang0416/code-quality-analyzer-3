import heapq

def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    N = int(input[idx])
    idx += 1
    M = int(input[idx])
    idx += 1

    adj = [[] for _ in range(N+1)]  # 1-based

    for _ in range(M):
        c = int(input[idx])
        idx +=1
        r = int(input[idx])
        idx +=1
        d = int(input[idx])
        idx +=1
        s = int(input[idx])
        idx +=1
        adj[c].append( (r, s, d) )
    
    a = list(map(int, input[idx:idx+N]))
    idx 