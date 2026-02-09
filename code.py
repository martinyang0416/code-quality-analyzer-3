import bisect

class SegmentTree:
    def __init__(self, size):
        self.n = 1
        while self.n < size:
            self.n <<= 1
        self.size = size
        self.tree = [-float('inf')] * (2 * self.n)

    def update_point(self, pos, value):
        pos += self.n
        self.tree[pos] = value
        pos >>= 1
        while pos >= 1:
            new_val = max(self.tree[2 * pos], self.tree[2 * pos + 1])
            if self.tree[pos] == new_val:
                break
            self.