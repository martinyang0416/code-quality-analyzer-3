def main():
    import sys
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    counts = [0] * 31  # since integers are 32-bit, but 0-30 is sufficient

    for num in arr:
        for i in range(31):
            if num & (1 << i):
                counts[i] += 1

    total = 0
    for i in range(31):
        c = counts[i]
        if c >= 2:
            total += (c * (c - 1) // 2) * (1 << i)
    
    print(total)

if __name__ == "__main__":
    main()