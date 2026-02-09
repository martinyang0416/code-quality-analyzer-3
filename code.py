def subarrayBitwiseORs(A):
    global_set = set()
    prev = set()
    for num in A:
        current = {num}
        for x in prev:
            current.add(x | num)
        prev = current
        global_set.update(current)
    return len(global_set)