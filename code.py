from collections import deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    N = int(data[idx])
    idx += 1
    u = int(data[idx])
    idx += 1
    v = int(data[idx])
    idx += 1
    
    adj = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a = int(data[idx])
        idx += 1
        b = int(data[idx])
        idx += 1
        adj[a].append(b)
        adj[b].append(a)
    
    # Compute d_v and parent using BFS from v
    d_v = [-1]