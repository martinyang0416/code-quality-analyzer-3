def ceildiv(a, b):
    if b == 0:
        return 0 if a == 0 else float('inf')
    return (a + b - 1) // b

def putaway(A, B, T, X, Y, W, S):
    eligible_weak = [False] * T
    eligible_small = [False] * T

    for i in range(T):
        w = W[i]
        s_val = S[i]
        ew = False
        if A > 0:
            for x in X:
                if x > w:
                    ew = True
                    break
        eligible_weak[i] = ew

        es = False
        if B > 0:
            for y in