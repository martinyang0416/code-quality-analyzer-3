m, p, q, t = map(int, input().split())

total = t ** q

if m > total:
    print(-1)
else:
    packages = []
    for i in range(m):
        number = i
        digits = []
        for _ in range(q):
            digits.append(number % t)
            number = number // t
        digits = digits[::-1]  # Reverse to get the correct order
        truck_assignment = [d + 1 for d in digits]
        packages.append(truck_assignment)
    
    for day in range(q):
        line = ' '.join(map(str, [pkg[day] 