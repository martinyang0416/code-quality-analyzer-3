MOD = 10**9 + 7
inv2 = 500000004  # Modular inverse of 2 mod 1e9+7

def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr])
    ptr +=1
    for _ in range(T):
        n = int(input[ptr])
        ptr +=1
        P = list(map(int, input[ptr:ptr+n]))
        ptr +=n
        A = list(map(int, input[ptr:ptr+n]))
        ptr +=n
        B = list(map(int, input[ptr:ptr+n]))
        ptr +=n
        
        all_zero = all(b == 0 for b in B)
        if all_zero