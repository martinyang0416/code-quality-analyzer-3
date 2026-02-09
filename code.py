def consecutiveNumbersSum(N):
    count = 0
    k = 1
    while True:
        temp = N - k * (k - 1) // 2
        if temp <= 0:
            break
        if temp % k == 0:
            count += 1
        k += 1
    return count