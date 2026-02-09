from collections import Counter

def numTilePossibilities(tiles: str) -> int:
    counts = Counter(tiles)
    
    def backtrack(counts_dict):
        total = 0
        for char in counts_dict:
            if counts_dict[char] == 0:
                continue
            counts_dict[char] -= 1
            total += 1  # Current character forms a new sequence
            total += backtrack(counts_dict)
            counts_dict[char] += 1
        return total
    
    return backtrack(counts)