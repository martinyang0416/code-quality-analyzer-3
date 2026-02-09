def count_odd_pairs(s):
    even = 0
    odd = 0
    for char in s:
        pos = ord(char) - ord('a') + 1
        if pos % 2 == 0:
            even += 1
        else:
            odd += 1
    return even * odd

T = int(input())
for _ in range(T):
    S = input().strip()
    print(count_odd_pairs(S))