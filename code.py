from collections import defaultdict

def uniqueLetterString(s: str) -> int:
    MOD = 10**9 + 7
    char_positions = defaultdict(list)
    n = len(s)
    
    for i, char in enumerate(s):
        char_positions[char].append(i)
    
    total = 0
    for char, indices in char_positions.items():
        m = len(indices)
        for i in range(m):
            current = indices[i]
            prev = indices[i-1] if i > 0 else -1
            next_ = indices[i+1] if i < m - 1 else n
            total 