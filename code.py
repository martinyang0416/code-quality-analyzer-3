import sys

def main():
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        m = int(line.strip())
        if m == 0:
            break
        # Read constellation points
        constellation = []
        for _ in range(m):
            x, y = map(int, sys.stdin.readline().split())
            constellation.append((x, y))
        # Read photo points
        n = int(sys.stdin.readline())
        photo = []
        photo_set = set()
        for _ in r