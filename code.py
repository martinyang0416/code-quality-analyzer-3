t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    day_max = {}
    for _ in range(n):
        d, b = map(int, input().split())
        if d in day_max:
            if b > day_max[d]:
                day_max[d] = b
        else:
            day_max[d] = b
    max_beauties = list(day_max.values())
    if len(max_beauties) < 2:
        print(0)
    else:
        sorted_max = sorted(max_beauties, reverse=True)
        print(sorted_max[0] + sorted_max[1])