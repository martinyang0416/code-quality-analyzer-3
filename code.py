n = int(input())
b = list(map(int, input().split()))
a = list(map(int, input().split()))

# Convert to 1-based indexing
b = [0] + b
a = [0] + a

x = [0] * (n + 1)
k = [0] * (n + 1)

for i in range(2, n + 1):
    xi, ki = map(int, input().split())
    x[i] = xi
    k[i] = ki

for i in range(n, 0, -1):
    if i == 1:
        if a[i] > b[i]:
            print("NO")
            exit()
    else:
        if b[i] >= a[i]:
            surplus = b[i] - a[i]
            b[x[i]] += surplus
        else:
  