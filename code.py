def putaway(A, B, T, X, Y, W, S):
    # Compute maximum X and Y
    max_x = -float('inf')
    if A > 0:
        max_x = max(X)
    else:
        max_x = -float('inf')
        
    max_y = -float('inf')
    if B > 0:
        max_y = max(Y)
    else:
        max_y = -float('inf')
    
    # Check each toy and count Mw, Ms, and possible assignments
    Mw = 0  # toys only possible for weak
    Ms = 0  # toys only possible for small
    possible = True  # flag for feasibility
    
    for i in range