s = input().strip()
parts = s.split('+')
parts.sort()
print('+'.join(parts))