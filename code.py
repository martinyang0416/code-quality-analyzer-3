from collections import Counter

n = int(input())
cards = [int(input()) for _ in range(n)]
freq = Counter(cards)

unique = list(freq.keys())
found = False
result = []

half = n // 2

for i in range(len(unique)):
    for j in range(i + 1, len(unique)):
        x = unique[i]
        y = unique[j]
        if freq[x] == half and freq[y] == half:
            found = True
            result = [x, y]
            break
    if found:
        break

if found:
    print("YES")
    print(f"{result[0]} {resu