import sys

def main():
    input = sys.stdin.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        A = int(input[idx])
        B = int(input[idx+1])
        C = int(input[idx+2])
        idx +=3
        a = 'K' if A % 3 == 0 else 'X'
        b = 'G' if B % 5 == 0 else 'Y'
        c = 'B' if C % 2 == 0 else 'Z'
        print(f"{a}-{b}-{c}")

if __name__ == "__main__":
    main()