def main():
    import sys
    s = sys.stdin.readline().strip()
    target = list("bessie")
    n = len(s)
    if n < 6:
        print(0)
        return

    total = 0
    pos = [-1] * 6  # pos[i] is the current index for the ith character of target
    current_start = -1

    for i in range(n):
        c = s[i]
        # Iterate backwards to prevent overwriting
        for j in range(5, -1, -1):
            if c == target[j]:
                if j == 0:
                    pos[0] = i
           