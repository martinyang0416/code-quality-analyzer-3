n, l = map(int, input().split())
a = list(map(int, input().split()))
max_ai = max(a) if a else 0
max_area = 0

for d in range(l, max_ai + 1):
    total = sum(ai // d for ai in a)
    if total == 0:
        continue
    area = total * d
    if area > max_area:
        max_area = area

print(max_area)