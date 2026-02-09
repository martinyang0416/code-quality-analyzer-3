t = int(input())
test_cases = []
max_N = 0
for _ in range(t):
    n = int(input())
    test_cases.append(n)
    if n > max_N:
        max_N = n

k_max = max_N - 1

if k_max < 0:
    dp = [0]
else:
    dp = [0] * (k_max + 1)
    dp[0] = 1
    if k_max >= 1:
        dp[1] = 1
    if k_max >= 2:
        dp[2] = 1
    for k in range(3, k_max + 1):
        dp[k] = dp[k - 1] + dp[k - 3]

for n in test_cases:
    k = n - 1
    if k < 0:
        print(0)
    else:
        print(dp[k])