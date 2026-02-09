n = int(input())
coins = [int(input()) for _ in range(n)]
total = sum(coins)
half = total // 2

possible_sums = {0}
for v in coins:
    sums_to_add = list(possible_sums)
    for s in sums_to_add:
        new_sum = s + v
        if new_sum <= half:
            possible_sums.add(new_sum)

max_sum = max(possible_sums)
min_diff = total - 2 * max_sum
print(min_diff)