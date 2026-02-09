def find_mth_number(M):
    if M == 0:
        return 0
    digits = []
    while M > 0:
        rem = M % 7
        digits.append(str(rem))
        M = M // 7
    digits.reverse()
    return int(''.join(digits))

M = int(input())
print(find_mth_number(M))