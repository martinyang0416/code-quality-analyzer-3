s = input().strip()
mod = 10**9 + 7

segments = s.split('b')
result = 1

for seg in segments:
    cnt = seg.count('a')
    if cnt:
        result = (result * (cnt + 1)) % mod

print((result - 1) % mod)