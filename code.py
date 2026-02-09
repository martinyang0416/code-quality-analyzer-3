s = input().strip()

runs = []
current_char = s[0]
count = 1

for c in s[1:]:
    if c == current_char:
        count += 1
    else:
        runs.append(count)
        current_char = c
        count = 1
runs.append(count)

total = sum(1 for x in runs if x % 2 == 0)
print(total)