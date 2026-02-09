MOD = 10**9 + 7

class Solution:
    def countSubstrings(self, s: str) -> int:
        current = 0
        total = 0
        for c in s:
            if c == '1':
                current += 1
            else:
                total += current * (current + 1) // 2
                current = 0
        total += current * (current + 1) // 2
        return total % MOD