import bisect
from collections import deque

def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    w = int(input[ptr]); ptr +=1
    h = int(input[ptr]); ptr +=1
    n = int(input[ptr]); ptr +=1
    flower_beds = []
    for _ in range(n):
        x1 = int(input[ptr]); ptr +=1
        y1 = int(input[ptr]); ptr +=1
        x2 = int(input[ptr]); ptr +=1
        y2 = int(input[ptr]); ptr +=1
        flower_beds.append( (x1, y1, x2, y2) )
    
    # Collect x and y coordinate