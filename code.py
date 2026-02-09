M = int(input())
lines = []
for _ in range(M):
    d, c = map(int, input().split())
    lines.append((d, c))

number_str = ''.join(str(d) * c for d, c in lines)
rounds = 0

while len(number_str) > 1:
    sum_digits = sum(int(ch) for ch in number_str)
    rounds += 1
    number_str = str(sum_digits)

print(rounds)