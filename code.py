from collections import defaultdict, deque

class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        # Preprocess B to get indices for each character
        b_indices = defaultdict(deque)
        for idx, char in enumerate(B):
            b_indices[char].append(idx)
        
        # Build the permutation array
        permutation = []
        for char in A:
            permutation.append(b_indices[char].popleft())
        
        # Find cycles in the permutation and calculat