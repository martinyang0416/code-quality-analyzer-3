def main():
    import sys
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowel_indices = []
    for i, c in enumerate(s):
        if c in vowels:
            vowel_indices.append(i)
    v = len(vowel_indices)
    print(v * (v + 1) // 2)

if __name__ == "__main__":
    main()