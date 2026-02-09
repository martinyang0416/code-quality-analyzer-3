def makesquare(matchsticks):
    total = sum(matchsticks)
    if total % 4 != 0:
        return False
    target = total // 4
    matchsticks.sort(reverse=True)
    if not matchsticks or matchsticks[0] > target:
        return False
    sides = [0] * 4

    def backtrack(index):
        if index == len(matchsticks):
            return all(side == target for side in sides)
        current = matchsticks[index]
        seen = set()
        for i in range(4):
            if sides[i] + current > targ