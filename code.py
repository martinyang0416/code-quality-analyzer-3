def minAddToMakeValid(S):
    balance = 0
    ans = 0
    for c in S:
        if c == '(':
            balance += 1
        else:
            balance -= 1
            if balance < 0:
                ans += 1
                balance += 1
    return ans + balance