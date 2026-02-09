import sys

def generate_pairings(lst):
    if not lst:
        return [ [] ]
    first = lst[0]
    res = []
    for i in range(1, len(lst)):
        pair = (first, lst[i])
        remaining = lst[1:i] + lst[i+1:]
        for rest in generate_pairings(remaining):
            res.append([pair] + rest)
    return res

def canonical_partition(pairs):
    sorted_pairs = [tuple(sorted(p)) for p in pairs]
    sorted_pairs.sort()
    return tuple(sorted_pairs)

def main():
    # Precompute all possibl