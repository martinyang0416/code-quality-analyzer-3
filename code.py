def putaway(A, B, T, X, Y, W, S):
    if A == 0 and B == 0:
        return -1  # according to problem constraints, this case won't occur
    
    # Compute maximum values for weak and small robots
    maxX = -float('inf')
    if A > 0:
        maxX = max(X)
    maxY = -float('inf')
    if B > 0:
        maxY = max(Y)
    
    S_only = 0
    W_only = 0
    both = 0
    valid = True
    
    for i in range(T):
        w = W[i]
        s = S[i]
        cw = (A != 0) and (w < maxX)
        cs = (B !