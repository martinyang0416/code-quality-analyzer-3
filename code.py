def putaway(A, B, T, X, Y, W, S):
    # Check if each toy can be assigned to at least one robot
    can0 = False
    can1 = False

    # Check for toy 0
    if A > 0:
        for x in X:
            if W[0] < x:
                can0 = True
                break
    if not can0 and B > 0:
        for y in Y:
            if S[0] < y:
                can0 = True
                break
    if not can0:
        return -1

    # Check for toy 1
    if A > 0:
        for x in X:
            if W[1] < x: