import sys

def query(c, d):
    print(f"? {c} {d}")
    sys.stdout.flush()
    return int(sys.stdin.readline())

a = 0
b = 0

res = query(0, 0)
if res == 0:
    print(f"! {a} {b}")
    sys.exit()

# Find the highest differing bit
m = 29
for bit in range(29, -1, -1):
    new_res = query(a ^ (1 << bit), b)
    if new_res != res:
        m = bit
        break

# Determine the m-th bit (a has 1, b has 0)
a ^= (1 << m)

# Determine remaining bits
for bit in range(m-1, -1, -1):
    # Check a's bit
  