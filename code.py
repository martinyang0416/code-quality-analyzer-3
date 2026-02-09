def check_valid_groups(temp_list):
    groups = []
    i = 0
    n = len(temp_list)
    while i < n:
        if i + 3 < n:
            current = temp_list[i:i+4]
            if len(set(current)) == 1:
                groups.append(current)
                i += 4
                continue
            if current == sorted(current) and current[0] == current[3] - 3:
                groups.append(current)
                i += 4
                continue
        if i + 3 >= n:
            return False
 