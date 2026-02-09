def putaway(A, B, T, X, Y, W, S):
    if T != 2 or (A + B) != 2:
        # According to the problem's subproblem constraints, we only handle T=2 and A+B=2
        # In actual submission, this might be handled differently, but for the subproblem:
        return -1  # This is a safety net

    can_weak = [False] * 2
    can_small = [False] * 2

    for i in range(2):
        # Check if the toy can be handled by any weak robot
        can_weak[i] = any(W[i] < x for x in X) if A > 0 else False
     