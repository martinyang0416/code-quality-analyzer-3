def isValid(s):
    stack = []
    for c in s:
        stack.append(c)
        while len(stack) >= 3 and stack[-3:] == ['a', 'b', 'c']:
            del stack[-3:]
    return not stack