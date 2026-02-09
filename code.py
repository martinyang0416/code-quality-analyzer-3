def countTriplets(arr):
    n = len(arr)
    prefix_xor = [0]
    for num in arr:
        prefix_xor.append(prefix_xor[-1] ^ num)
    res = 0
    for i in range(n):
        for k in range(i, n):
            if prefix_xor[i] == prefix_xor[k+1]:
                res += (k - i)
    return res