from typing import List

class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        waiting = 0
        boarded = 0
        rotations = 0
        max_profit = -float('inf')
        best_rotations = -1
        i = 0
        n = len(customers)
        
        while i < n or waiting > 0:
            if i < n:
                waiting += customers[i]
                i += 1
            
            boarding = min(4, waiting)
       