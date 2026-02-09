import bisect

def main():
    import sys
    input = sys.stdin.read().split()
    t = list(input[0])
    U = int(input[1])
    updates = []
    for i in range(U):
        p = int(input[2*i + 2])
        c = input[2*i + 3]
        updates.append((p-1, c))  # converting to 0-based index

    target = 'bessie'

    def compute_instances(s):
        instances = []
        pos = [-1] * 6
        total = 0
        n = len(s)
        for i in range(n):
            c = s[i]
            for k in range(5