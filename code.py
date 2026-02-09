def superPow(a, b):
    mod = 1337
    a_mod = a % mod
    result = 1
    for digit in b:
        result = (pow(result, 10, mod) * pow(a_mod, digit, mod)) % mod
    return result