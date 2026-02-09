def decode_binary_string(s):
    result = []
    for i in range(0, len(s), 4):
        chunk = s[i:i+4]
        low, high = 0, 16
        for bit in chunk:
            mid = (low + high) // 2
            if bit == '0':
                high = mid
            else:
                low = mid
        result.append(chr(ord('a') + low))
    return ''.join(result)

T = int(input())
for _ in range(T):
    N = int(input())
    S = input().strip()
    print(decode_binary_string(S))