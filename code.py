def putaway(A, B, T, X, Y, W, S):
    if A == 0 and B == 0:
        return -1  # problem constraints say A+B >=1
    
    max_x = 0
    if A > 0:
        max_x = max(X)
    max_y = 0
    if B > 0:
        max_y = max(Y)
    
    a_count = 0
    b_count = 0
    both_count = 0
    
    for i in range(T):
        can_weak = False
        if A > 0 and W[i] < max_x:
            can_weak = True
        can_small = False
        if B > 0 and S[i] < max_y:
            can_small = True
        if can_wea