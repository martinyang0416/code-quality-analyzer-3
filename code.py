import sys
from itertools import combinations

def main():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n, c, q = map(int, input[ptr:ptr+3])
        ptr +=3
        p = list(map(int, input[ptr:ptr+n]))
        ptr +=n
        queries = []
        for __ in range(q):
            i, j = map(int, input[ptr:ptr+2])
            ptr +=2
            queries.append( (i-1, j) )  # converting to 0-based index
        
        # Genera