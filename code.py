n = int(input())
left0 = 0
left1 = 0
right0 = 0
right1 = 0

for _ in range(n):
    l, r = map(int, input().split())
    if l == 0:
        left0 += 1
    else:
        left1 += 1
    if r == 0:
        right0 += 1
    else:
        right1 += 1

left_min = min(left0, left1)
right_min = min(right0, right1)
print(left_min + right_min)