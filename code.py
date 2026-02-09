def main():
    import sys

    prefix = "What are you doing while sending "  # 33 characters
    middle_str = "? Are you busy? Will you send "  # 26 characters
    f0_str = "What are you doing at the end of the world? Are you busy? Will you save us?"

    q = int(sys.stdin.readline())
    output = []

    for _ in range(q):
        n, k = map(int, sys.stdin.readline().split())
        current_level = n
        current_k = k

        while current_level > 0:
            if current_k <= 33:
     