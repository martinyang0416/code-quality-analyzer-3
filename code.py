import sys
sys.setrecursionlimit(1 << 25)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1

    parent = [i for i in range(n + 1)]  # 1-based indexing
    rank = [1] * (n + 1)

    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u

    def union(u, v):
        u_root = find(u)
        v_root = find(v)
  