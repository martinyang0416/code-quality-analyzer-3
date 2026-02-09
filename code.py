import sys

def main():
    n, q = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    max_a = max(a) if a else 0

    def compute_mobius(max_mobius):
        if max_mobius < 1:
            return []
        spf = list(range(max_mobius + 1))
        for i in range(2, int(max_mobius**0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, max_mobius + 1, i):
                    if spf[j] == j:
                        spf[j] = i
    