def numSteps(s):
    def add_one(s):
        s_list = list(s)
        carry = 1
        i = len(s_list) - 1
        while i >= 0 and carry:
            total = int(s_list[i]) + carry
            if total == 2:
                s_list[i] = '0'
                carry = 1
            else:
                s_list[i] = '1'
                carry = 0
            i -= 1
        if carry:
            s_list.insert(0, '1')
        return ''.join(s_list)
    
    def count_trailing_zeros(s):
        count = 