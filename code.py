from functools import lru_cache

class Solution:
    def minDays(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def dfs(remaining):
            if remaining <= 1:
                return remaining
            option1 = 1 + dfs(remaining - 1)
            option2 = (remaining % 2) + 1 + dfs(remaining // 2)
            option3 = (remaining % 3) + 1 + dfs(remaining // 3)
            return min(option1, option2, option3)
        
        return dfs(n)