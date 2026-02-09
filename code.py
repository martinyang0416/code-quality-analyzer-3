import bisect
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    ptr = 1

    # Initialize a dictionary to hold for each x its list of dates and prefix sums
    warehouse = defaultdict(lambda: ([], []))  # [dates, sums]

    for _ in range(n):
        a = int(data[ptr])
        d = int(data[ptr+1])
        x = int(data[ptr+2])
        ptr += 3

        if a == 1 or a == 2:
            delta = 1 if a == 1 