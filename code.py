MOD = 10**9 + 7

def sumSubarrayMins(A):
    n = len(A)
    PLE = [-1] * n
    NLE = [n] * n
    stack = []
    
    for i in range(n):
        while stack and A[stack[-1]] >= A[i]:
            stack.pop()
        if stack:
            PLE[i] = stack[-1]
        stack.append(i)
    
    stack = []
    for i in range(n-1, -1, -1):
        while stack and A[stack[-1]] > A[i]:
            stack.pop()
        if stack:
            NLE[i] = stack[-1]
        stack.append(i)
    
    total = 0
    for