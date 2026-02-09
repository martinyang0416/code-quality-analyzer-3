import sys

def main():
    valid = {1, 2, 145, 40585}
    input = sys.stdin.read().split()
    T = int(input[0])
    results = []
    for n_str in input[1:T+1]:
        n = int(n_str)
        results.append(1 if n in valid else 0)
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()