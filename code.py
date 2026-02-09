import sys

users = set()
total = 0

for line in sys.stdin:
    line = line.rstrip('\n')
    if line.startswith('+'):
        users.add(line[1:])
    elif line.startswith('-'):
        users.remove(line[1:])
    else:
        sender, message = line.split(':', 1)
        total += len(message) * len(users)

print(total)