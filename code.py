class Solution:
    def rob(self, nums: list[int]) -> int:
        def helper(subnums):
            prev, curr = 0, 0
            for num in subnums:
                prev, curr = curr, max(curr, prev + num)
            return curr
        
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(helper(nums[:-1]), helper(nums[1:]))