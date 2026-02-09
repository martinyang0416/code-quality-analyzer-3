import sys

def main():
    input = sys.stdin.read
    data = input().split()
    ptr = 0
    T = int(data[ptr])
    ptr += 1
    for _ in range(T):
        n = int(data[ptr])
        m = int(data[ptr+1])
        ptr +=2
        edges = []
        for i in range(m):
            u = int(data[ptr])
            v = int(data[ptr+1])
            edges.append((u, v))
            ptr +=2
        used = [False] * (3 * n + 2)
        matching = []
        for i in range(m):
            u, v = edges[i]
  