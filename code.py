n = int(input())
total = 0.0
for _ in range(n):
    score = float(input())
    total += score
average = total / n
adjusted_average = average + 10
print("{0:.2f}".format(round(adjusted_average, 2)))