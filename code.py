import sys

data = [line.strip() for line in sys.stdin if line.strip()]
ptr = 0
T = int(data[ptr])
ptr += 1
for _ in range(T):
    N = int(data[ptr])
    ptr += 1
    names = data[ptr:ptr + N]
    ptr += N
    unique_sorted = sorted(set(names))
    for name in unique_sorted:
        print(name)