import sys

def is_convex(points):
    cross = []
    for i in range(4):
        p = points[i]
        q = points[(i+1)%4]
        r = points[(i+2)%4]
        dx1 = q[0] - p[0]
        dy1 = q[1] - p[1]
        dx2 = r[0] - q[0]
        dy2 = r[1] - q[1]
        cross_val = dx1 * dy2 - dy1 * dx2
        cross.append(cross_val)
    if all(c >= 0 for c in cross) or all(c <= 0 for c in cross):
        return "YES"
    else:
        return "NO"

for line in sys.stdin:
    data = list(map(float, line