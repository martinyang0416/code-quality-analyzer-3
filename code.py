t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        row = []
        for j in range(m):
            if (i + j) % 2 == 0:
                if a[i][j] % 2 == 0:
                    row.append(a[i][j])
                else:
                    row.append(a[i][j] + 1)
            else:
                if a[i][j] % 2 == 1:
                    row.append(a[i][j])
                else:
       