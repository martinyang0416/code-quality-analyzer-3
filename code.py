# Read the number of test cases
T = int(input())
for _ in range(T):
    # Read N and S for each test case
    N, S = map(int, input().split())
    # Read the list of prices
    P = list(map(int, input().split()))
    # Read the list of types (0 for defender, 1 for forward)
    types = list(map(int, input().split()))
    
    # Separate the players into defenders and forwards based on their type
    defenders = []
    forwards = []
    for price, t in zip(P, types):
        if t == 0:
           