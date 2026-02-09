n = int(input())
coords = list(map(int, input().split()))
x = coords[::2]
y = coords[1::2]
min_x = min(x)
max_x = max(x)
min_y = min(y)
max_y = max(y)
area = (max_x - min_x) * (max_y - min_y)
print(area)