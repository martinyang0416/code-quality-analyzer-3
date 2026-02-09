MOD = 10**9 + 7

class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        A.sort()
        s = set(A)
        dp = {x: 1 for x in A}
        
        for x in A:
            for a in A:
                if a > x:
                    break
                if x % a != 0:
                    continue
                b = x // a
                if b not in s:
                    continue
                if a > b:
                    continue
                if a == b:
       