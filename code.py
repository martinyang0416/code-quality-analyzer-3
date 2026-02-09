b = int(input())
m = input().strip()

if m == '0':
    print(0)
else:
    res = 0
    for c in m:
        d = int(c)
        res = res * b + d
    print(res)