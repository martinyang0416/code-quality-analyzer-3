n, m, q = map(int, input().split())
count1 = 0  # even i and even j
count2 = 0  # odd i and odd j

for _ in range(q):
    i, j = map(int, input().split())
    if i % 2 == 0 and j % 2 == 0:
        count1 += 1
    else:
        count2 += 1
    if count1 == 0 or count2 == 0:
        print("YES")
    else:
        print("NO")