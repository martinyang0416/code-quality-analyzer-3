def putaway(A, B, T, X, Y, W, S):
    if T != 2 or (A + B) != 2:
        return -1  # according to problem constraints, but code is for subcase
    
    # Check each toy can be handled by at least one robot
    for i in range(2):
        can_weak = False
        can_small = False
        if A > 0:
            for x in X:
                if W[i] < x:
                    can_weak = True
                    break
        if B > 0:
            for y in Y:
                if S[i] < y:
               