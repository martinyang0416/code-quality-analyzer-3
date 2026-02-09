import sys
from functools import lru_cache

def main():
    N, M = map(int, sys.stdin.readline().split())

    @lru_cache(maxsize=None)
    def dfs(remaining_product, remaining_count):
        if remaining_count == 0:
            return remaining_product == 1
        if remaining_product == 0:
            return False
        max_a = min(M, remaining_product)
        for a in range(1, max_a + 1):
            if remaining_product % a == 0:
                if dfs(remaining_product // a, remaining_