def putaway(A, B, T, X, Y, W, S):
    if T == 0:
        return 0  # Edge case if no toys, though constraints say T >=1
    
    maxWeak = 0
    if A > 0:
        maxWeak = max(X)
    maxSmall = 0
    if B > 0:
        maxSmall = max(Y)
    
    count_only_weak = 0
    count_only_small = 0
    count_both = 0
    
    for i in range(T):
        can_weak = (A > 0) and (W[i] < maxWeak)
        can_small = (B > 0) and (S[i] < maxSmall)
        
        if not can_weak and not can_small:
            