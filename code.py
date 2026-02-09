import sys

def main():
    n = int(sys.stdin.readline())
    l = list(map(int, sys.stdin.readline().split()))
    m = max(l)
    s = sum(l)
    
    # Option 1: Z <= current maximum
    option1_val = max(1, 2 * m - s + 1)
    candidate1 = option1_val if option1_val <= m else float('inf')
    
    # Option 2: Z becomes new maximum
    option2_val = m + 1
    candidate2 = option2_val if s > option2_val else float('inf')
    
    minimal_z = min(candidate1, candidate2)
    print(minimal_z)

if __n