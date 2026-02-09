def hIndex(citations):
    n = len(citations)
    left, right = 0, n - 1
    res = -1
    while left <= right:
        mid = (left + right) // 2
        if citations[mid] >= (n - mid):
            res = mid
            right = mid - 1
        else:
            left = mid + 1
    if res == -1:
        return 0
    return n - res