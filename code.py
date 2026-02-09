import sys
import math
import random

def main():
    n = int(sys.stdin.readline())
    factors = set()

    def send_query(query):
        print(query)
        sys.stdout.flush()
        return int(sys.stdin.readline())

    def factor(m):
        if m == 1:
            return
        if m in factors:
            return
        d = find_divisor(m)
        if d is None:
            factors.add(m)
            return
        factor(d)
        factor(m // d)

    def find_divisor(m):
        s = se