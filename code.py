def decimal_to_septenary(n):
    if n == 0:
        return '0'
    is_negative = False
    if n < 0:
        is_negative = True
        n = -n
    digits = []
    while n > 0:
        digits.append(str(n % 7))
        n = n // 7
    res = ''.join(reversed(digits))
    if is_negative:
        res = '-' + res
    return res

nums = []
for num in map(int, input().split()):
    if num == -1:
        break
    nums.append(num)

septenary = [decimal_to_septenary(num) for num in nums]
print(' '.join(se