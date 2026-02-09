allowed = {'3', '4', '6', '7'}
s = input().strip()
print("Yes" if all(c in allowed for c in s) else "No")