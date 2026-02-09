import sys

rect_count = 0
rhombus_count = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    a, b, c = map(int, line.split(','))
    if a**2 + b**2 == c**2:
        rect_count += 1
    if a == b:
        rhombus_count += 1

print(rect_count)
print(rhombus_count)