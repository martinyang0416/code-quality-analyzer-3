def trap(height):
    if not height:
        return 0
    left = 0
    right = len(height) - 1
    left_max = right_max = result = 0
    while left <= right:
        if left_max <= right_max:
            if height[left] > left_max:
                left_max = height[left]
            else:
                result += left_max - height[left]
            left += 1
        else:
            if height[right] > right_max:
                right_max = height[right]
            else:
                result