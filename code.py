n = int(input())
if n == 0:
    print(0)
    exit()
a = list(map(int, input().split()))
dp = [float('inf')] * n
dp[0] = 1  # The first element requires one stroke

for i in range(1, n):
    for j in range(i, -1, -1):
        if a[j] != a[i]:
            break
        if j == 0:
            cost = 1
        else:
            cost = dp[j - 1] + 1
        if cost < dp[i]:
            dp[i] = cost

print(dp[-1])