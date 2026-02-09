def mincostTickets(days, costs):
    travel_days = set(days)
    max_day = days[-1]
    dp = [0] * (max_day + 1)
    
    for day in range(1, max_day + 1):
        if day not in travel_days:
            dp[day] = dp[day - 1]
        else:
            cost1 = dp[day - 1] + costs[0]
            cost7 = costs[1] if day - 7 < 0 else dp[day - 7] + costs[1]
            cost30 = costs[2] if day - 30 < 0 else dp[day - 30] + costs[2]
            dp[day] = min(cost1, cost7, cost30)
    
    return dp[max_