def solve(a):
    binary = bin(a)[2:].zfill(6)
    product = 1
    for i in range(6):
        if binary[i] == '1':
            product *= (6 - i)  # positions counted from the right (starting at 1)
    return product

# Read input and print output
a = int(input())
print(solve(a))