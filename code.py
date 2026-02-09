x, y, z = map(int, input().split())
min_profit = min(x, y, z)
if x == min_profit:
    print("Apple")
elif y == min_profit:
    print("Banana")
else:
    print("Cherry")