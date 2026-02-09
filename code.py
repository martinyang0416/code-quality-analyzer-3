import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        a = list(map(int, sys.stdin.readline().split()))
        s = [(i + x) % n for i, x in enumerate(a)]
        freq = [0] * n
        valid = True
        for num in s:
            if freq[num] != 0:
                valid = False
                break
            freq[num] += 1
        print("YES" if valid else "NO")

if __name__ == "__main__":
    main()