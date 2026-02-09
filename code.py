mod = 15746
n = int(input())
if n == 0:
    print(1 % mod)
else:
    a, b = 1, 1
    for i in range(2, n + 1):
        a, b = b, (a + b) % mod
    print(b)