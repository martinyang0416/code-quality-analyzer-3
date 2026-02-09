from collections import Counter

k = int(input())
s = input().strip()

total_length = len(s)
if total_length % k != 0:
    print(-1)
else:
    cnt = Counter(s)
    possible = True
    for c, count in cnt.items():
        if count % k != 0:
            possible = False
            break
    if not possible:
        print(-1)
    else:
        base = []
        for char in sorted(cnt.keys()):
            base.append(char * (cnt[char] // k))
        base_str = ''.join(base)
        result = base_st