t = int(input())
for _ in range(t):
    n = int(input())
    first_chars = []
    for _ in range(n):
        city = input().strip()
        first_chars.append(city[0])
    if len(first_chars) == len(set(first_chars)):
        print("YES")
    else:
        print("NO")