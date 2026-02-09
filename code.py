n = int(input())
s = list(map(int, input().split()))
swaps = []
for i in range(n):
    for j in range(n - i - 1):
        if s[j] > s[j + 1]:
            # Swap the elements
            s[j], s[j + 1] = s[j + 1], s[j]
            # Record the swap using 1-based indices
            swaps.append((j + 1, j + 2))
# Print each swap
for swap in swaps:
    print(swap[0], swap[1])