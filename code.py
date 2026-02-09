def main():
    import sys
    N = int(sys.stdin.readline())
    result = []
    for _ in range(N):
        parts = list(map(int, sys.stdin.readline().split()))
        a, b, c, d, e = parts
        bits = []
        # Process first three numbers (a, b, c)
        for num in [a, b, c]:
            # Convert each number to two bits (LSB first)
            bits.append(num & 1)          # LSB
            bits.append((num >> 1) & 1)   # MSB
        # Process last two numbers (d, e)
        for num i