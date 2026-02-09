from collections import Counter

def findLeastNumOfUniqueInts(arr, k):
    freq = Counter(arr)
    sorted_freq = sorted(freq.values())
    removed = 0
    for f in sorted_freq:
        if k >= f:
            k -= f
            removed += 1
        else:
            break
    return len(freq) - removed