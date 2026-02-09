def minCost(s, cost):
    total = 0
    prev_char = s[0]
    sum_group = cost[0]
    max_group = cost[0]
    
    for i in range(1, len(s)):
        if s[i] == prev_char:
            sum_group += cost[i]
            if cost[i] > max_group:
                max_group = cost[i]
        else:
            total += sum_group - max_group
            prev_char = s[i]
            sum_group = cost[i]
            max_group = cost[i]
    
    total += sum_group - max_group
    return total