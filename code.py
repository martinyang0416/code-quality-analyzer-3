def main():
    import sys
    A = "What are you doing while sending \""
    B = '"? Are you busy? Will you send "'
    C = '"?'
    f0 = "What are you doing at the end of the world? Are you busy? Will you save us?"

    q = int(sys.stdin.readline())
    output = []
    for _ in range(q):
        n, k = map(int, sys.stdin.readline().split())
        if k < 1:
            output.append('.')
            continue
        # Check if k > L_n
        if n > 60:
            # L_n is way larger than 1e1