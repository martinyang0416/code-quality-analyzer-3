def main():
    import sys
    s = sys.stdin.readline().strip()
    n = len(s)
    # Initialize DP table where dp[i][j] indicates if s[i..j] is a palindrome
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                if length == 2 or dp[i+1][j-1]:
                    dp[i][j] = 1
            else:
                dp[i][j] = 0