import bisect

def putaway(A, B, T, X, Y, W, S):
    X_sorted = sorted(X)
    Y_sorted = sorted(Y)
    
    can_weak = [False] * T
    can_small = [False] * T
    
    for i in range(T):
        w = W[i]
        idx = bisect.bisect_right(X_sorted, w)
        can_weak[i] = (idx < len(X_sorted))
        
        s = S[i]
        idx = bisect.bisect_right(Y_sorted, s)
        can_small[i] = (idx < len(Y_sorted))
        
        if not (can_weak[i] or can_small[i]):
            return -1
    
    o