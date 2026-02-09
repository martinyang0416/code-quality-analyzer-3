def main():
    import sys
    input = sys.stdin.read().split('\n')
    idx = 0
    T = int(input[idx].strip())
    idx += 1
    for _ in range(T):
        # Read N, K, initial Answer
        while idx < len(input) and input[idx].strip() == '':
            idx += 1
        n, k, ans = map(int, input[idx].split())
        idx += 1
        # Read array A
        while idx < len(input) and input[idx].strip() == '':
            idx += 1
        a = list(map(int, input[idx].split()))
        idx += 1