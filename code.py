import sys

def main():
    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr])
    ptr += 1
    for _ in range(T):
        N, M, K = map(int, input[ptr:ptr+3])
        ptr += 3
        A = list(map(int, input[ptr:ptr+N]))
        ptr += N
        B = []
        for _ in range(N):
            row = list(map(int, input[ptr:ptr+M]))
            B.append(row)
            ptr += M
        C = []
        for _ in range(N):
            row = list(map(int, input[ptr:ptr+M]))
          