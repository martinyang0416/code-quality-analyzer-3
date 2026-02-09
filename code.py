import sys

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        if line == '0':
            break
        N = int(line)
        days = []
        valid = True
        # Read N days and check validity
        for _ in range(N):
            # Read next non-empty line
            while True:
                curr_line = sys.stdin.readline()
                if not curr_line:
                    break
                curr_line = curr_lin