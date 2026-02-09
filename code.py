n = int(input())
scores = list(map(int, input().split()))
scores.sort()
mid = n // 2
lower = scores[mid - 1]
upper = scores[mid]
count = upper - lower
print(count if count >= 0 else 0)