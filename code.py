import itertools

def maxAbsValExpr(arr1, arr2):
    max_diff = 0
    for signs in itertools.product([1, -1], repeat=3):
        s1, s2, s3 = signs
        values = [s1 * a + s2 * b + s3 * i for i, (a, b) in enumerate(zip(arr1, arr2))]
        current_max = max(values)
        current_min = min(values)
        diff = current_max - current_min
        if diff > max_diff:
            max_diff = diff
    return max_diff