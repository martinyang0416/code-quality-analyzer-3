def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n ** 0.5) + 1
    for i in range(3, max_divisor, 2):
        if n % i == 0:
            return False
    return True

n = int(input())
count = 0
for _ in range(n):
    num = int(input())
    if is_prime(num):
        count += 1
print(count)