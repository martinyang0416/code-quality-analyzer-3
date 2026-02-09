n = int(input())
prefs = [list(map(int, input().split())) for _ in range(n)]
gift = [0] * (n + 1)
used = set()

for i in range(1, n + 1):
    for j in prefs[i - 1]:
        if j != i and j not in used:
            gift[i] = j
            used.add(j)
            break

print(' '.join(map(str, gift[1:])))