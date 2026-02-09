def main():
    import sys

    part1 = "What are you doing while sending "  # ends with a space (33 characters)
    part2 = " Are you busy? Will you send "     # ends with a space (28 characters)
    f0 = "What are you doing at the end of the world? Are you busy? Will you save us?"  # 71 characters

    # Precompute lengths
    part1_len = len(part1)
    part2_len = len(part2)
    f0_len = len(f0)

    q = int(sys.stdin.readline())
    res = []

    for _ in range(q):
        n, k = map(int, sy