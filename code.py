def singleNumber(nums):
    result = 0
    for i in range(32):
        sum_bit = 0
        for num in nums:
            sum_bit += (num >> i) & 1
        sum_bit %= 3
        if sum_bit:
            result |= (sum_bit << i)
    if result >= (1 << 31):
        result -= (1 << 32)
    return result