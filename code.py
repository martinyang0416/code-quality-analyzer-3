while True:
    n = int(input())
    if n == 0:
        break
    moves = input().split()
    left = 'floor'
    right = 'floor'
    state = 'floor'
    count = 0
    for move in moves:
        if move == 'lu':
            left = 'step'
        elif move == 'ru':
            right = 'step'
        elif move == 'ld':
            left = 'floor'
        elif move == 'rd':
            right = 'floor'
        # Check state transitions
        if state == 'floor' and left == 'step' and right == 'step'