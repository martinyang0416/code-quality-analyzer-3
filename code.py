def compute_sum(a, b, c):
    if b < c:
        n = b - a + 1
        first = c - b
        last = c - a
        return (first + last) * n // 2
    elif a > c:
        n = b - a + 1
        first = a - c
        last = b - c
        return (first + last) * n // 2
    else:
        left_part = c - a
        left_sum = left_part * (left_part + 1) // 2
        right_part = b - c
        right_sum = right_part * (right_part + 1) // 2
        return left_sum + right_sum

n, K = map(int, input().split