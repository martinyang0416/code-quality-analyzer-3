def split_array(nums, m):
    left = max(nums)
    right = sum(nums)
    
    while left < right:
        mid = (left + right) // 2
        current_sum = 0
        splits = 1
        
        for num in nums:
            if current_sum + num > mid:
                splits += 1
                current_sum = num
            else:
                current_sum += num
        
        if splits <= m:
            right = mid
        else:
            left = mid + 1
    
    return left