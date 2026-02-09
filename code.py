n = int(input())
prefixes = []
suffixes = []
max_streaks = []
is_full_list = []

for _ in range(n):
    s = input().strip()
    # Compute prefix
    prefix = 0
    for c in s:
        if c == 'C':
            prefix += 1
        else:
            break
    prefixes.append(prefix)
    
    # Compute suffix
    suffix = 0
    for c in reversed(s):
        if c == 'C':
            suffix += 1
        else:
            break
    suffixes.append(suffix)
    
    # Compute max streak
    max_streak = 