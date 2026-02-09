def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    t = int(input[idx])
    idx += 1
    for _ in range(t):
        n = int(input[idx])
        k = int(input[idx + 1])
        idx += 2
        arr = list(map(int, input[idx:idx + n]))
        idx += n

        # Find the top k elements
        top_k = sorted(arr, reverse=True)[:k]
        top_set = set(top_k)
        count = 0
        for num in arr[:k]:
            if num in top_set:
                count += 1
       