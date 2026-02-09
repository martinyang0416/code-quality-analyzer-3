s = input().strip()
a = c = m = 0
for char in s:
    if char == 'A':
        a += 1
    elif char == 'C':
        c += a
    elif char == 'M':
        m += c
print(m)