def wordBreak(s, wordDict):
    word_set = set(wordDict)
    max_length = max(len(word) for word in word_set) if word_set else 0
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True  # Empty string can be segmented
    
    for i in range(1, n + 1):
        start = max(0, i - max_length)
        for j in range(start, i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break  # No need to check further once found
    return dp[n]