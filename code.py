import sys

def main():
    input = sys.stdin.read
    data = input().split()
    T = int(data[0])
    index = 1
    for _ in range(T):
        N = int(data[index])
        B = int(data[index + 1])
        index += 2
        if B == 0:
            print(0)
            continue
        max_y = N // B
        y_opt_floor = N // (2 * B)
        candidates = [y_opt_floor - 1, y_opt_floor, y_opt_floor + 1]
        max_val = 0
        for y in candidates:
            if y < 0 or y > max_y:
           