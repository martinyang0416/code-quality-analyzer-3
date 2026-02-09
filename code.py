def maxSumDivThree(nums):
    total = sum(nums)
    remainder = total % 3
    if remainder == 0:
        return total
    
    mod1 = sorted(num for num in nums if num % 3 == 1)
    mod2 = sorted(num for num in nums if num % 3 == 2)
    
    possible = []
    if remainder == 1:
        if mod1:
            possible.append(mod1[0])
        if len(mod2) >= 2:
            possible.append(mod2[0] + mod2[1])
    else:  # remainder == 2
        if mod2:
            possible.append(mod2[0])
        if 