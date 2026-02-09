import bisect

def putaway(A, B, T, X, Y, W, S):
    sorted_X = sorted(X)
    sorted_Y = sorted(Y)

    only_weak = 0
    only_small = 0
    both = 0
    weak_eligible = []
    small_eligible = []

    for w, s in zip(W, S):
        can_weak = False
        can_small = False

        if A > 0:
            pos = bisect.bisect_right(sorted_X, w)
            if pos < A:
                can_weak = True
        if B > 0:
            pos = bisect.bisect_right(sorted_Y, s)
            if pos < B:
     