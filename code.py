from functools import cmp_to_key

def largestNumber(nums):
    strs = list(map(str, nums))
    
    def compare(a, b):
        if a + b > b + a:
            return -1
        else:
            return 1
    
    strs.sort(key=cmp_to_key(compare))
    result = ''.join(strs)
    return '0' if result[0] == '0' else result