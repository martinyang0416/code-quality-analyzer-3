def canConvert(s: str, t: str, k: int) -> bool:
    if len(s) != len(t):
        return False
    
    shifts = []
    for sc, tc in zip(s, t):
        diff = (ord(tc) - ord(sc)) % 26
        if diff != 0:
            shifts.append(diff)
    
    from collections import Counter
    counts = Counter(shifts)
    
    for r in counts:
        if r > k:
            return False
        available = (k - r) // 26 + 1
        if counts[r] > available:
            return False
    
    return True