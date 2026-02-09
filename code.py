n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print("1 1")
    print(-a[0])
    print("1 1")
    print(0)
    print("1 1")
    print(0)
else:
    # Operation 1: zero the first element
    print("1 1")
    print(-a[0])
    a[0] = 0

    # Operation 2: handle elements 2 to n
    print(f"2 {n}")
    ks = []
    add_op2 = []
    for i in range(1, n):
        k = a[i] % n
        ks.append(k)
        add_op2.append(k * (n-1))
    print(' '.join(map(str, add_op2)))

    # Operat