# Read the number of test cases
T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    if n == 1:
        print(0)
    else:
        print(m * (n - 1))