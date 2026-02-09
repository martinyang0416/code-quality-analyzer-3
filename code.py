def jump(nums):
    jumps = 0
    current_end = 0
    max_far = 0
    n = len(nums)
    for i in range(n - 1):
        max_far = max(max_far, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = max_far
            if current_end >= n - 1:
                break
    return jumps