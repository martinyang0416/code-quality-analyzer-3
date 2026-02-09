from collections import Counter

def canReorderDoubled(arr):
    count = Counter(arr)
    for x in sorted(arr, key=lambda x: abs(x)):
        if count[x] == 0:
            continue
        required = 2 * x
        if count[required] < count[x]:
            return False
        count[required] -= count[x]
        count[x] = 0
    return True