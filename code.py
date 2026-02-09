def putaway(A, B, T, X, Y, W, S):
    # Pre-check if all toys are assignable
    maxWeakX = max(X) if A > 0 else -1
    maxSmallY = max(Y) if B > 0 else -1

    for i in range(T):
        w = W[i]
        s = S[i]
        can_weak = (A > 0 and w < maxWeakX)
        can_small = (B > 0 and s < maxSmallY)
        if not can_weak and not can_small:
            return -1

    # Sort robots and toys
    sorted_weak = sorted(X)
    sorted_small = sorted(Y)

    # Sort toys by weight for weak processing