a1, a2, k = map(int, input().split())

def compute_fib_pair(n):
    if n == 0:
        return (0, 0)
    a, b = 0, 1  # fib(0) and fib(1)
    if n == 1:
        return (a, b)
    for i in range(2, n + 1):
        next_val = a + b
        a, b = b, next_val
    return (a, b)

fib_prev, fib_k = compute_fib_pair(k)
result = a1 * fib_prev + a2 * fib_k
print(result)