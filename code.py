def main():
    import sys
    s = sys.stdin.read().strip()
    target = ['b', 'e', 's', 's', 'i', 'e']
    n = len(target)
    dp = [0] * (n + 1)
    dp[0] = 1
    total = 0

    for c in s:
        new_dp = dp.copy()
        for i in range(n, 0, -1):
            if c == target[i-1]:
                new_dp[i] += new_dp[i-1]
        dp = new_dp
        total += dp[n]
    print(total)

if __name__ == "__main__":
    main()