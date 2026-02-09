import sys

def main():
    import sys
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    prefix = [0]
    for num in a:
        prefix.append(prefix[-1] + num)
    
    for i in range(1, n + 1):
        # Generate A_sums: subarrays including i
        A_sums = []
        for l in range(1, i + 1):
            for r in range(i, n + 1):
                A_sums.append(prefix[r] - prefix[l - 1])
        
        # Generate B_sums: subarrays not including i
    