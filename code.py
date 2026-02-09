def main():
    import sys
    letter = sys.stdin.readline().strip()
    phrase = sys.stdin.readline().strip()
    
    p = len(phrase)
    n = len(letter)
    count = 0
    
    if p == 0 or n < p:
        print(0)
        return
    
    for i in range(n - p + 1):
        valid = True
        for j in range(p):
            c = letter[i + j]
            required = phrase[j]
            if c != '$' and c != required:
                valid = False
                break
        if valid:
         