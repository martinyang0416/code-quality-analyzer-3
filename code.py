def minimumOneBitOperations(n):
    if n == 0:
        return 0
    k = n.bit_length() - 1
    return (1 << (k + 1)) - 1 - minimumOneBitOperations(n - (1 << k))