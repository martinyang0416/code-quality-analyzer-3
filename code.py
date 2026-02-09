a = int(input())
if a < 10:
    sum_digits = a
else:
    sum_digits = a // 10 + a % 10
print("YES" if sum_digits % 5 == 0 else "NO")