def main():
    import sys
    N = int(sys.stdin.readline())
    output = []
    for _ in range(N):
        parts = list(map(int, sys.stdin.readline().split()))
        a, b, c, d, e = parts
        numbers = [a, b, c, d, e]
        bits = []
        for num in numbers:
            # Convert number to 2-bit binary string, pad with leading zeros if needed
            b_str = bin(num)[2:].zfill(2)
            # Reverse the bits
            reversed_b = b_str[::-1]
            bits.append(reversed_