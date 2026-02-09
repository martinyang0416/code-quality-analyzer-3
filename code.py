import sys

class TrieNode:
    __slots__ = ['children']
    def __init__(self):
        self.children = [None, None]  # children for 0 and 1

def main():
    input = sys.stdin.read().split()
    idx = 0
    C = int(input[idx])
    idx += 1
    N = int(input[idx])
    idx += 1

    all_masks = []
    for _ in range(N):
        s = input[idx]
        idx += 1
        bits = tuple(0 if c == 'G' else 1 for c in s)
        all_masks.append(bits)
    
    unique_masks = list(set(all_masks))
    
    