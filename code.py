from collections import deque

s = input().strip()
n = len(s)
if n == 0:
    print(0)
    exit()

prev = [i - 1 for i in range(n)]
next = [i + 1 if i < n - 1 else -1 for i in range(n)]
current_queue = deque()

for i in range(n):
    left = prev[i]
    right = next[i]
    has_diff = False
    if left != -1 and s[left] != s[i]:
        has_diff = True
    if not has_diff and right != -1 and s[right] != s[i]:
        has_diff = True
    if has_diff:
        current_queue.append(i)

deleted = [False