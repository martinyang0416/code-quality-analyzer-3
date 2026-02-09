import sys

def main():
    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr])
    ptr += 1
    for _ in range(T):
        n, k = map(int, input[ptr:ptr+2])
        ptr += 2
        Q = list(map(int, input[ptr:ptr+n]))
        ptr += n
        carry = 0
        found = False
        for i in range(n):
            total = carry + Q[i]
            if total < k:
                print(i + 1)
                found = True
                break
            carry = total - k
        if