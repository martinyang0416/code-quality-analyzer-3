def isRationalEqual(S: str, T: str) -> bool:
    def parse(s):
        if '.' in s:
            int_part, frac_part = s.split('.', 1)
            if '(' in frac_part:
                split_idx = frac_part.index('(')
                non_rep = frac_part[:split_idx]
                rep = frac_part[split_idx+1:-1]
            else:
                non_rep = frac_part
                rep = ''
            return int_part, non_rep, rep
        else:
            return s, '', ''
    
    def to_frac(int