n, k = map(int, input().split())
a = list(map(int, input().split()))
current_sum = sum(abs(a[i] - a[i+1]) for i in range(n-1))

for _ in range(k):
    best_delta = 0
    best_i = -1
    best_j = -1
    for i in range(n):
        for j in range(i+1, n):
            # Calculate affected pairs
            affected = set()
            if i > 0:
                affected.add((i-1, i))
            if i < n-1:
                affected.add((i, i+1))
            if j > 0:
                affected.add((j-1