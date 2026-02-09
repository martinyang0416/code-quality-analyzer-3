n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

total = 0

# Calculate sum of B values
for a in A:
    total += B[a - 1]

# Check consecutive dishes for C bonuses
for i in range(n - 1):
    current = A[i]
    next_dish = A[i + 1]
    if next_dish == current + 1:
        total += C[current - 1]

print(total)