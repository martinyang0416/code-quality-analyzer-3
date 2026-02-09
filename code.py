def main():
    s = input().strip()
    n = len(s)
    if n <= 1:
        print("YES")
        return
    # Determine the direction between the first two characters
    prev_dir = None
    for i in range(1, n):
        current_diff = ord(s[i]) - ord(s[i-1])
        if current_diff == 0:
            print("NO")
            return
        current_dir = current_diff > 0
        if prev_dir is not None:
            if current_dir == prev_dir:
                print("NO")
                return
      