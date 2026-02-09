y = input().strip()
mod_value = 0
for ch in y:
    mod_value = (mod_value * 10 + int(ch)) % 7
print(mod_value)