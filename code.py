import sys

def main():
    input = sys.stdin.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        S = int(input[idx])
        SG = int(input[idx+1])
        FG = int(input[idx+2])
        D = int(input[idx+3])
        T_val = int(input[idx+4])
        idx +=5
        
        actual = S + (180 * D) / T_val
        diff_sebi = abs(SG - actual)
        diff_father = abs(FG - actual)
        
        if diff_sebi < diff_father:
            print("SEBI")
        elif diff