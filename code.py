def smallest_repunit_divisible_by_k(K):
    if K % 2 == 0 or K % 5 == 0:
        return -1
    mod_val = 9 * K
    current = 1
    for m in range(1, mod_val + 1):
        current = (current * 10) % mod_val
        if current == 1:
            return m
    return -1