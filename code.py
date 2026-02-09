def maximumGap(nums):
    n = len(nums)
    if n < 2:
        return 0
    min_val = min(nums)
    max_val = max(nums)
    if min_val == max_val:
        return 0
    bucket_count = n - 1
    buckets = [{'min': None, 'max': None} for _ in range(bucket_count)]
    
    for x in nums:
        if x == max_val:
            bucket_idx = bucket_count - 1
        else:
            bucket_idx = ((x - min_val) * bucket_count) // (max_val - min_val)
        if bucket_idx >= bucket_count:
            bucke