from collections import Counter

t = input().strip()
p = input().strip()
permutation = list(map(int, input().split()))  # This is not used in the solution

count_p = Counter(p)
sum_p = sum(count_p.values())
max_remove = len(t) - sum_p

print(max_remove)