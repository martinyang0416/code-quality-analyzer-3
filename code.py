import bisect

def count_balanced_substrings(s):
    n = len(s)
    count_4 = [0] * (n + 1)
    for i in range(1, n+1):
        count_4[i] = count_4[i-1] + (1 if s[i-1] == '4' else 0)
    ans = 0
    for L in range(1, n+1):
        a = count_4[L-1]
        # Binary search for the smallest R >= L where count_4[R] > a
        # The count_4 array is non-decreasing, so we can use bisect
        # We need to search in the subarray count_4[L..n]
        # Using bisect_right to find the first element >