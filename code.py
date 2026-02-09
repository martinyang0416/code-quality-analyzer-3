def fractionToDecimal(numerator: int, denominator: int) -> str:
    if numerator == 0:
        return "0"
    
    res = []
    if (numerator < 0) ^ (denominator < 0):
        res.append('-')
    
    numerator = abs(numerator)
    denominator = abs(denominator)
    
    integer_part = numerator // denominator
    remainder = numerator % denominator
    res.append(str(integer_part))
    
    if remainder == 0:
        return ''.join(res)
    
    res.append('.')
    
    remainder_map = {}
    
