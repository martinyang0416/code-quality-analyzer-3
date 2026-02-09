def solve(a):
    # Convert to binary with 6 bits, padding with leading zeros if necessary
    bits = bin(a)[2:].zfill(6)
    product = 1
    for i in range(6):
        if bits[i] == '1':
            # The position is i+1 since it starts from 1
            product *= (i + 1)
    return product

# Read input and output
a = int(input())
print(solve(a))