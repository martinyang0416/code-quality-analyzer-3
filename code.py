MOD = 998244353
MAX = 10**6  # Adjust based on constraints to avoid MLE, but 1e6 is manageable.

# Precompute factorial, inverse factorial, and inverses up to MAX
fact = [1] * (MAX)
for i in range(1, MAX):
    fact[i] = fact[i-1] * i % MOD

inv_fact = [1] * (MAX)
inv_fact[MAX-1] = pow(fact[MAX-1], MOD-2, MOD)
for i in range(MAX-2, -1, -1):
    inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

def C(n, k):
    if n < 0 or k < 0 or n < k:
        return 0
    return fact[n] * inv_fact[k] % MOD * inv_fact