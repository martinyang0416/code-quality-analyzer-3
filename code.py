def main():
    import sys
    input = sys.stdin.read().split()
    T = int(input[0])
    cases = list(map(float, input[1:T+1]))
    
    for S in cases:
        valid = []
        for h in range(12):
            for m in range(60):
                total = 30.0 * h + 6.5 * m
                if abs(total - S) <= 0.1:
                    valid.append((h, m))
        # Prepare output
        output = []
        for h, m in valid:
            hh = f"{h:02d}"
            mm = f"{m:02d}"
            o