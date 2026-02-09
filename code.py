def previous_permutation(s):
    s = list(s)
    n = len(s)
    
    # Step 1: Find the largest index k such that s[k] > s[k+1]
    k = n - 2
    while k >= 0 and s[k] <= s[k + 1]:
        k -= 1
    
    if k == -1:
        return None  # No previous permutation exists
    
    # Step 2: Find the largest index j > k such that s[j] < s[k]
    j = n - 1
    while s[j] >= s[k]:
        j -= 1
    
    # Step 3: Swap s[k] and s[j]
    s[k], s[j] = s[j], s[k]
    
    # Step 4: Reverse the suffix st