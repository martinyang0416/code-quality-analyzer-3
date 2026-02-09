from functools import lru_cache

def countArrangement(n: int) -> int:
    @lru_cache(maxsize=None)
    def backtrack(pos, used_mask):
        if pos > n:
            return 1
        count = 0
        for num in range(1, n+1):
            if not (used_mask & (1 << (num-1))):
                if num % pos == 0 or pos % num == 0:
                    count += backtrack(pos + 1, used_mask | (1 << (num-1)))
        return count
    return backtrack(1, 0)