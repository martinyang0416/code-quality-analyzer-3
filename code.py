n = int(input())
scores = list(map(int, input().split()))
scores.sort()

max_rating = 0
for R in range(n, 0, -1):
    # Binary search to find the first index where score >= R
    left, right = 0, n
    while left < right:
        mid = (left + right) // 2
        if scores[mid] >= R:
            right = mid
        else:
            left = mid + 1
    count = n - left
    if count >= R:
        max_rating = R
        break

print(max_rating)