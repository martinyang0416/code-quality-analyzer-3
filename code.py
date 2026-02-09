import bisect

n, k, s, t = map(int, input().split())
cars = [tuple(map(int, input().split())) for _ in range(n)]
g = list(map(int, input().split()))

# Process checkpoints and compute segments
checkpoints = [0] + g + [s]
checkpoints.sort()
segments = []
for i in range(1, len(checkpoints)):
    segments.append(checkpoints[i] - checkpoints[i-1])

segments.sort()

# Compute prefix sums and max_gap
prefix = [0]
current_sum = 0
for d in segments:
    current_sum += d
    prefix.append(current_sum)
s