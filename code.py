MOD = 10**9 + 7
max_pow = 10**5  # Since n can be up to 1e5, n-L can be up to 1e5 -1
pow26 = [1] * (max_pow + 1)

for i in range(1, max_pow + 1):
    pow26[i] = (pow26[i-1] * 26) % MOD

T = int(input())
for case in range(1, T+1):
    n, m = map(int, input().split())
    patterns = [input().strip() for _ in range(m)]
    print(f"Case {case}:")
    for s in patterns:
        L = len(s)
        if L > n:
            print(0)
        else:
            e = n - L
            res = ((n - L + 1) * pow26