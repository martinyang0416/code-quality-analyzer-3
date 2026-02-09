def findLUSlength(strs):
    def is_subsequence(s, t):
        it = iter(t)
        return all(c in it for c in s)
    
    max_length = -1
    for i in range(len(strs)):
        is_candidate = True
        for j in range(len(strs)):
            if i == j:
                continue
            if is_subsequence(strs[i], strs[j]):
                is_candidate = False
                break
        if is_candidate:
            current_length = len(strs[i])
            if current_length > max_length: