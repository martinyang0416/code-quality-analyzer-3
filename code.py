from collections import deque

def findMinStep(board: str, hand: str) -> int:
    def collapse(s):
        while True:
            groups = []
            n = len(s)
            i = 0
            while i < n:
                current = s[i]
                j = i
                while j < n and s[j] == current:
                    j += 1
                if j - i >= 3:
                    groups.append((i, j-1))
                i = j
            if not groups:
                break
            to_r