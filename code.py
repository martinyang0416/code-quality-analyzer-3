import sys

def main():
    n = int(sys.stdin.readline())
    objects = []
    for _ in range(n):
        parent, typ = map(int, sys.stdin.readline().split())
        objects.append((parent, typ))
    
    # Precompute type0_parent and part_leader
    type0_parent = [-1] * (n + 1)
    part_leader = [0] * (n + 1)
    for i in range(1, n + 1):
        parent, typ = objects[i-1]
        if parent != -1:
            if typ == 0:
                type0_parent[i] = parent
            else:
            