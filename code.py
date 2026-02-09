import heapq

h, w, K = map(int, input().split())
grid = []
s_pos = None
e_pos = None
a_positions = []
for i in range(h):
    row = list(input().strip().replace(' ', ''))
    for j in range(w):
        if row[j] == 's':
            s_pos = (i, j)
        elif row[j] == 'e':
            e_pos = (i, j)
        elif row[j] == 'a':
            a_positions.append((i, j))
    grid.append(row)

m = len(a_positions)
if m < K:
    print(-1)
    exit()

a_index = {pos: idx for idx, pos in enumerate(a_posi