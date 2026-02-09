import sys

def main():
    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr])
    ptr += 1
    for _ in range(T):
        N = int(input[ptr])
        ptr += 1
        X = []
        H = []
        for _ in range(N):
            x = int(input[ptr])
            h = int(input[ptr + 1])
            X.append(x)
            H.append(h)
            ptr += 2
        c = [0] * N
        for j in range(N):
            if j == 0:
                c[j] = X[1] - X[0]
            elif j == N