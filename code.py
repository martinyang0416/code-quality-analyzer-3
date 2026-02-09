n = int(input())
winners = [int(input().strip()) for _ in range(n)]

current_players = [1, 2]
spectator = 3
valid = True

for a in winners:
    if a not in current_players:
        valid = False
        break
    if current_players[0] == a:
        other = current_players[1]
    else:
        other = current_players[0]
    next_players = [a, spectator]
    spectator = other
    current_players = next_players

print("YES" if valid else "NO")