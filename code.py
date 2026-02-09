n = int(input())
s = input().strip()

zeros = s.count('0')
ones = len(s) - zeros

if zeros != ones:
    print(1)
    print(s)
else:
    for i in range(1, len(s)):
        s1 = s[:i]
        z1 = s1.count('0')
        o1 = i - z1
        if z1 != o1:
            print(2)
            print(f"{s1} {s[i:]}")
            break