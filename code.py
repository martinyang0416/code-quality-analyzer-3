import bisect

def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr])
    ptr += 1
    for _ in range(T):
        N = int(input[ptr])
        ptr += 1
        min_b = {}
        for _ in range(N):
            a = int(input[ptr])
            b = int(input[ptr+1])
            ptr +=2
            if a in min_b:
                if b < min_b[a]:
                    min_b[a] = b
            else:
                min_b[a] = b
        sorted_ab = sorted(min_b