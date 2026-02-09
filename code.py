t = int(input())
for _ in range(t):
    s = input().strip()
    k = int(input())
    
    # Generate all unique substrings
    substrs = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n + 1):
            substr = s[i:j]
            substrs.add(substr)
    
    # Sort substrings in reverse lexicographical order
    substr_list = sorted(substrs, reverse=True)
    
    # Concatenate all substrings
    concatenated = ''.join(substr_list)
    
    # Get the k-th character
 