from collections import defaultdict

def subarraysWithKDistinct(A, K):
    def atMost(k):
        freq = defaultdict(int)
        left = 0
        count = 0
        res = 0
        for right in range(len(A)):
            if freq[A[right]] == 0:
                count += 1
            freq[A[right]] += 1
            while count > k:
                freq[A[left]] -= 1
                if freq[A[left]] == 0:
                    count -= 1
                left += 1
            res += right - left + 1
