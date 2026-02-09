from collections import defaultdict

def reorderedPowerOf2(N):
    # Precompute the power_map once per function call (inefficient but acceptable)
    power_map = defaultdict(set)
    exp = 0
    while True:
        current_power = 2 ** exp
        s = str(current_power)
        length = len(s)
        if length > 10:
            break
        sorted_str = ''.join(sorted(s))
        power_map[length].add(sorted_str)
        exp += 1
    
    s = str(N)
    sorted_n = ''.join(sorted(s))
    length