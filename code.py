n = int(input())
p = list(map(int, input().split()))

pos = [0] * (n + 1)  # 1-based indexing for values
for i in range(n):
    val = p[i]
    pos[val] = i  # 0-based index

class FenwickTree:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (self.n + 2)  # 1-based indexing

    def update(self, idx):
        while idx <= self.n:
            self.tree[idx] += 1
            idx += idx & -idx

    def query(self, idx):
        res = 0
        while idx > 0:
           