n = int(input())
s = list(input().strip())

carry = True
count = 0
pos = n - 1  # Start at the LSB (last character)

while pos >= 0 and carry:
    current = s[pos]
    # Toggle the bit
    if current == '1':
        s[pos] = '0'
    else:
        s[pos] = '1'
    count += 1

    # Determine if carry continues
    if current == '1':
        carry = True
    else:
        carry = False

    pos -= 1

print(count)