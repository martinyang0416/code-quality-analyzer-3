n = int(input())
cards = set()

for _ in range(n):
    s, r = input().split()
    cards.add((s, int(r)))

missing = []
for suit in ['S', 'H', 'C', 'D']:
    for rank in range(1, 14):
        if (suit, rank) not in cards:
            missing.append(f"{suit} {rank}")

for card in missing:
    print(card)