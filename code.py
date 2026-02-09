t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    sum_a = sum(a) - max(a)
    sum_b = sum(b) - max(b)
    if sum_a < sum_b:
        print("Alice")
    elif sum_a > sum_b:
        print("Bob")
    else:
        print("Draw")