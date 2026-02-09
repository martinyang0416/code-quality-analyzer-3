def maxCoins(piles):
    piles.sort()
    total = 0
    n = len(piles) // 3
    for i in range(n):
        total += piles[len(piles) - 2 * (i + 1)]
    return total