from collections import defaultdict

def find_lex_smallest_A(S):
    # Calculate the required counts for each character in A
    char_count = defaultdict(int)
    for c in S:
        char_count[c] += 1
    required = {k: v // 2 for k, v in char_count.items()}
    
    # Precompute suffix counts for each position
    n = len(S)
    suffix_counts = [defaultdict(int) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        # Copy previous counts
        for key in suffix_counts[i + 1]:
   