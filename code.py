def putaway(A, B, T, X, Y, W, S):
    if A == 0:
        max_x = -1
    else:
        max_x = max(X)
    
    if B == 0:
        max_y = -1
    else:
        max_y = max(Y)
    
    W_only = 0
    S_only = 0
    Both = 0

    for i in range(T):
        w = W[i]
        s = S[i]
        handle_weak = (A > 0 and w < max_x)
        handle_small = (B > 0 and s < max_y)
        
        if not handle_weak and not handle_small:
            return -1
        
        if handle_weak and handle_small:
  