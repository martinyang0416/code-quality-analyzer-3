s = input().strip()

mask = 0
dp = {0: 0}

for char in s:
    c = ord(char) - ord('a')
    mask ^= 1 << c
    min_val = float('inf')
    # Check current mask
    if mask in dp:
        min_val = dp[mask] + 1
    # Check all possible masks by flipping each bit
    for i in range(26):
        m = mask ^ (1 << i)
        current = dp.get(m, float('inf'))
        if current + 1 < min_val:
            min_val = current + 1
    # Update the current mask's value if needed
    current_mask_val = dp.get(