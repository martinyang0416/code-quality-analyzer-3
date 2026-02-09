import bisect

def maxProfitAssignment(difficulty, profit, worker):
    # Create a dictionary to map each difficulty to its maximum profit
    difficulty_profit = {}
    for d, p in zip(difficulty, profit):
        if d not in difficulty_profit or p > difficulty_profit[d]:
            difficulty_profit[d] = p
    
    # Sort the unique difficulties
    sorted_diffs = sorted(difficulty_profit.keys())
    
    # Create the max profit array
    max_profit = []
    current_max = 0
    for d in sorte