def min_changes(triplet, target_sum):
    sum_orig = sum(triplet)
    delta = target_sum - sum_orig
    if delta == 0:
        return 0
    delta_i_min = [-d for d in triplet]
    delta_i_max = [9 - d for d in triplet]
    for k in [1, 2, 3]:
        sorted_min = sorted(delta_i_min)
        min_d = sum(sorted_min[:k])
        sorted_max = sorted(delta_i_max, reverse=True)
        max_d = sum(sorted_max[:k])
        if min_d <= delta <= max_d:
            return k
    return 3

ticket = input().s