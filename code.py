n, s = map(int, input().split())
A = list(map(int, input().split()))
mod = 998244353

prev_count = [0] * (s + 1)
prev_sum_x1 = [0] * (s + 1)

answer = 0

for i in range(n):
    a = A[i]
    curr_count = [0] * (s + 1)
    curr_sum_x1 = [0] * (s + 1)
    
    if a <= s:
        curr_count[a] += 1
        curr_sum_x1[a] = (curr_sum_x1[a] + (i + 1)) % mod
    
    for s_prev in range(s + 1):
        if s_prev + a > s:
            continue
        s_new = s_prev + a
        curr_count[s_new] = (curr_