import bisect

def main():
    import sys
    s = sys.stdin.read().strip()
    n = len(s)
    
    # Initialize prefix arrays
    prefix_b = [0] * (n + 1)
    prefix_e = [0] * (n + 1)
    prefix_s = [0] * (n + 1)
    prefix_i = [0] * (n + 1)
    
    for i in range(n):
        prefix_b[i+1] = prefix_b[i] + (1 if s[i] == 'b' else 0)
        prefix_e[i+1] = prefix_e[i] + (1 if s[i] == 'e' else 0)
        prefix_s[i+1] = prefix_s[i] + (1 if s[i] == 's' else 0)
        prefix_i[i+1] = prefix_i[i] + 