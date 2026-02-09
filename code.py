n = int(input())
a = list(map(int, input().split()))

S = [i+1 for i, val in enumerate(a) if val == 1]
T = [i+1 for i, val in enumerate(a) if val == 0]

S.sort()
T.sort()

m = len(S)
k = len(T)

if m == 0:
    print(0)
    exit()

INF = 10**18

prev_dp = [0] * (k + 1)

for i in range(1, m + 1):
    curr_dp = [INF] * (k + 1)
    for j in range(1, k + 1):
        if j < i:
            curr_dp[j] = INF
            continue
        option1 = prev_dp[j-1] + abs(S[i-1] - T[j-1])
        option2 = curr