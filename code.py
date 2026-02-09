def max_substring(s, target, q):
    left = 0
    max_len = 0
    count = 0
    for right in range(len(s)):
        if s[right] != target:
            count += 1
        while count > q:
            if s[left] != target:
                count -= 1
            left += 1
        current = right - left + 1
        if current > max_len:
            max_len = current
    return max_len

def main():
    import sys
    n, q = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().strip()
 