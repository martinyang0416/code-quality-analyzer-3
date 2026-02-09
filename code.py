def largest_rectangle_area(heights):
    stack = [-1]
    max_area = 0
    for i in range(len(heights)):
        while stack[-1] != -1 and heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)
    while stack[-1] != -1:
        h = heights[stack.pop()]
        w = len(heights) - stack[-1] - 1
        max_area = max(max_area, h * w)
    return max_area

h, w = map(int, input().spl