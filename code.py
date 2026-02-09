k = int(input())
for i in range(1, k):
    row = []
    for j in range(1, k):
        if j == 0:
            row.append("N/A")
        elif i % j == 0:
            row.append(str(i // j))
        else:
            row.append("N/A")
    print(' '.join(row))