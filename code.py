n = int(input())
for _ in range(n):
    s = input().strip()
    if not s or s[0] == '0':
        print(0)
        continue
    max_len = len(s)
    for i in range(1, len(s)):
        if s[i-1] == '0' and s[i] == '1':
            max_len = i
            break
    count = s[:max_len].count('0')
    print(count)