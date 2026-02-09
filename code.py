def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    while True:
        N = int(input[ptr])
        ptr += 1
        if N == 0:
            break
        files = {}  # key: I, value: (start, end, E)
        excl_intervals = []
        free_intervals = [(0, float('inf'))]  # managed as list of (start, end), start <= end

        for _ in range(N):
            cmd = input[ptr]
            ptr += 1
            if cmd == 'W':
                I = int(input[ptr])
          