def longest_absolute_path(s):
    max_len = 0
    stack = []
    for line in s.split('\n'):
        depth = line.count('\t')
        name = line[depth:]
        while len(stack) > depth:
            stack.pop()
        current_length = len(name)
        if stack:
            current_length += stack[-1] + 1  # add parent's length and slash
        if '.' in name:
            max_len = max(max_len, current_length)
        else:
            stack.append(current_length)
    return max_len