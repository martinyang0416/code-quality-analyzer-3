MOD = 10**9 + 7
MAX_N = 200000  # Adjust this value based on expected constraints

# Precompute factorial and inverse factorial arrays
fact = [1] * (MAX_N + 1)
for i in range(1, MAX_N + 1):
    fact[i] = fact[i-1] * i % MOD

inv_fact = [1] * (MAX_N + 1)
# Compute inverse factorial of MAX_N first
inv_fact[MAX_N] = pow(fact[MAX_N], MOD-2, MOD)
for i in range(MAX_N - 1, -1, -1):
    inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

def comb(n, k):
    if n < 0 or k < 0 or k > n:
        return 0
    retur