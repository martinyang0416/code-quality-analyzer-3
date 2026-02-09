from collections import Counter

def main():
    s = input().strip()
    k = int(input())
    
    if not s:
        print(0)
        print()
        return
    
    freq = Counter(s)
    distinct = len(freq)
    
    if distinct <= k:
        print(len(s))
        print(s)
        return
    else:
        # Sort by frequency descending, then take top k
        letters = sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:k]
        selected_chars = {char for char, count in letters}
        total