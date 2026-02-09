def shipWithinDays(weights, D):
    left = max(weights)
    right = sum(weights)
    answer = right  # Initialize with the upper bound
    
    while left <= right:
        mid = (left + right) // 2
        days_needed = 1
        current_load = 0
        
        for weight in weights:
            if current_load + weight > mid:
                days_needed += 1
                current_load = 0
            current_load += weight
        
        if days_needed <= D:
            answer = mid
    