def numberOfGoodSplits(s):
    n = len(s)
    if n < 2:
        return 0
    
    # Compute left array using frequency counts
    left = []
    freq = [0] * 26
    distinct = 0
    for char in s:
        idx = ord(char) - ord('a')
        if freq[idx] == 0:
            distinct += 1
        freq[idx] += 1
        left.append(distinct)
    
    # Compute right array using frequency counts
    right = [0] * n
    freq_right = [0] * 26
    distinct_right = 0
    for i in reversed(range(n)):
       