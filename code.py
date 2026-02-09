n = int(input())
intervals = []
for _ in range(n):
    s, e = map(int, input().split())
    intervals.append((s, e))

def calculate_coverage(intervals_list):
    if not intervals_list:
        return 0
    sorted_intervals = sorted(intervals_list, key=lambda x: x[0])
    merged = []
    for interval in sorted_intervals:
        if not merged:
            merged.append(list(interval))
        else:
            last_start, last_end = merged[-1]
            current_start, current_end = interval
   