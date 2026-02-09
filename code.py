import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = list(map(int, line.split()))
    N = parts[0]
    nums = parts[1:1+N]
    evens = []
    for num in reversed(nums):
        if num % 2 == 0:
            evens.append(str(num))
    if not evens:
        print("None")
    else:
        print(' '.join(evens))