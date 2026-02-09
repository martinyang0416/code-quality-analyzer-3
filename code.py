n = int(input())
a = list(map(int, input().split()))
up = [1] * n
down = [1] * n

for i in range(n):
    for j in range(i):
        if a[j] < a[i]:
            if down[j] + 1 > up[i]:
                up[i] = down[j] + 1
        elif a[j] > a[i]:
            if up[j] + 1 > down[i]:
                down[i] = up[j] + 1

max_length = max(max(up), max(down))
print(max_length)