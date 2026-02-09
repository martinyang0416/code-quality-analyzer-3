def isValid(code):
    if not code.startswith('<') or len(code) < 2:
        return False
    
    first_close = code.find('>')
    if first_close == -1:
        return False
    start_tag = code[1:first_close]
    if not start_tag or len(start_tag) > 9 or not start_tag.isupper():
        return False
    
    expected_end = f'</{start_tag}>'
    if not code.endswith(expected_end):
        return False
    
    content = code[first_close + 1 : -len(expected_end)]
    stack = []
    i = 0
    n =