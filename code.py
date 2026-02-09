import sys

def main():
    input = sys.stdin.read().split()
    t = int(input[0])
    idx = 1
    for _ in range(t):
        m = int(input[idx])
        idx += 1
        if m == 2:
            print(1)
            print(2)
        else:
            k = m - 1
            print(k)
            print('1 ' * (m - 2) + '2')

if __name__ == "__main__":
    main()