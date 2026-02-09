import sys

data = list(map(int, sys.stdin.read().split()))
ptr = 0
T = data[ptr]
ptr += 1
for _ in range(T):
    N = data[ptr]
    ptr += 1
    max_h = max(data[ptr:ptr+N])
    ptr += N
    print(max_h)