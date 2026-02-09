def lastSubstring(s: str) -> str:
    n = len(s)
    best = 0
    for i in range(1, n):
        current_length = 0
        while True:
            if best + current_length >= n or i + current_length >= n:
                break
            if s[best + current_length] != s[i + current_length]:
                break
            current_length += 1
        if i + current_length >= n:
            continue
        if best + current_length >= n:
            best = i
            continue
        if s[i 