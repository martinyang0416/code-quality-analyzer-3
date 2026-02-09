import sys

def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def convex_hull(points):
    # Sort the points lexicographically (x then y)
    points = sorted(points)
    # Build lower part
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    # Build upper part
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upp