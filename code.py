def minNumber(num, k):
    def count_inversions(s):
        freq = [0] * 10
        inversions = 0
        for c in reversed(s):
            d = int(c)
            for i in range(d):
                inversions += freq[i]
            freq[d] += 1
        return inversions
    
    inversions = count_inversions(num)
    if k >= inversions:
        return ''.join(sorted(num))
    
    num_list = list(num)
    n = len(num_list)
    for i in range(n):
        if k <= 0:
            break
        j_ma