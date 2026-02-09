def longestMountain(A):
    max_len = 0
    up = 0
    down = 0
    n = len(A)
    if n < 3:
        return 0
    for i in range(1, n):
        if A[i] > A[i-1]:
            if down > 0:
                up = 0
                down = 0
            up += 1
        elif A[i] < A[i-1]:
            if up > 0:
                down += 1
                current = up + down + 1
                if current > max_len:
                    max_len = current
            else:
                up = 0
           