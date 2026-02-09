# Read the number of test cases
T = int(input())
for _ in range(T):
    s = input().strip()
    # Check if there are duplicate characters
    if len(set(s)) < len(s):
        print("yes")
    else:
        print("no")