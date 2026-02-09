import sys
import string
from collections import Counter

def process(s):
    s = s.lower()
    filtered = [c for c in s if c.isalpha()]
    return Counter(filtered)

def generate_pal(required):
    first_half = []
    middle = ''
    for char in string.ascii_lowercase:
        count = required[char]
        if count == 0:
            continue
        pairs = count // 2
        if pairs > 0:
            first_half.append(char * pairs)
        if count % 2 == 1 and not middle:
            middle 