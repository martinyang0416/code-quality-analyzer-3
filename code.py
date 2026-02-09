l, r = map(int, input().split())
n = int(input())

s = ''
for _ in range(n):
    parts = input().split()
    if parts[0] == 'append':
        s += parts[1]
    else:
        a, b = parts[1], parts[2]
        s = s.replace(a, b)

start = l - 1
end = r
if start < 0:
    start = 0
if end > len(s):
    end = len(s)
print(s[start:end])