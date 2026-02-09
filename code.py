class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        low = matrix[0][0]
        high = matrix[-1][-1]
        
        def count_less_equal(target):
            count = 0
            col = n - 1  # Start from the last column
            for row in matrix:
                while col >= 0 and row[col] > target:
                    col -= 1
                count += col + 1
            return count
        
        while low < high:
      