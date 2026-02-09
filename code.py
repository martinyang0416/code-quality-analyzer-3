c = list(map(int, input().split()))
total = sum(c)
if total == 0 or total % 5 != 0:
    print(-1)
else:
    print(total // 5)