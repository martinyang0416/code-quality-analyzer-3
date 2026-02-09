s = input().strip()
digits = s[1:]  # Extract the 6 digits after 'A'
first_two = int(digits[:2])
has_zero = '0' in digits
result = first_two - 1 if has_zero else first_two
print(result)