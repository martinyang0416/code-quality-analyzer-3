def findKthNumber(n: int, k: int) -> int:
    current = 1
    k -= 1  # convert to 0-based index
    while k > 0:
        steps = 0
        first = current
        last = current
        while first <= n:
            steps += min(last, n) - first + 1
            first *= 10
            last = last * 10 + 9
        if steps <= k:
            k -= steps
            current += 1
        else:
            k -= 1
            current *= 10
    return current