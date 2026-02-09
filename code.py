n = int(input())
heights = list(map(int, input().split()))
cores = []
for h in heights:
    core = h
    while core % 2 == 0:
        core //= 2
    cores.append(core)
print("YES" if all(c == cores[0] for c in cores) else "NO")