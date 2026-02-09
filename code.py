s = input().strip()
length = len(s)

# Calculate positions for first and last characters
first = ord(s[0]) - ord('A') + 1
last = ord(s[-1]) - ord('A') + 1

if length % 2 == 0:
    # Even length case
    if (first + last) % 2 == 0:
        print("YES")
    else:
        print("NO")
else:
    # Odd length case: check middle character and first+last
    mid_index = length // 2
    mid_char = s[mid_index]
    mid_val = ord(mid_char) - ord('A') + 1
    if (first + last) % 2 == 0 and mid_val % 2 == 0: