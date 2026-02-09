def putaway(A, B, T, X, Y, W, S):
    # Compute max_X and max_Y
    max_X = -1
    if A > 0:
        max_X = max(X)
    else:
        max_X = -1  # can_weak is False for all
    
    max_Y = -1
    if B > 0:
        max_Y = max(Y)
    else:
        max_Y = -1  # can_small is False for all
    
    # Count W_only, S_only, both
    W_only = 0
    S_only = 0
    both = 0
    for i in range(T):
        w = W[i]
        s = S[i]
        can_weak = (A > 0) and (w < max_X)
        can_small = (B > 0) a