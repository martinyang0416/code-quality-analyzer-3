def generate_all_matchings():
    elements = [1, 2, 3, 4, 5, 6]
    
    def helper(remaining):
        if not remaining:
            return [ [] ]
        first = remaining[0]
        results = []
        for i in range(1, len(remaining)):
            pair = (first, remaining[i])
            new_remaining = remaining[1:i] + remaining[i+1:]
            for sub in helper(new_remaining):
                results.append([pair] + sub)
        return results
    
    return helper(elements)

all_match