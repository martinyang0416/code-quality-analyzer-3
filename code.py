s = input().strip()
digits = list(map(int, s[1:]))
total = sum(digits)
if total < 20:
    print(2 * total - 1)
else:
    print(total + 1)