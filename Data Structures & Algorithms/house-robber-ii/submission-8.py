class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        n = len(nums)
        if n == 1:
            return nums[0]
        memo = {}
        def helper(nums, i):

            if i >= len(nums):
                return 0

            if i in memo:
                return memo[i]
            memo[i] = max(nums[i] + helper(nums, i + 2), helper(nums, i+1))
            return memo[i]

        case1 = helper(nums[1:], 0)
        memo = {}
        case2 = helper(nums[:-1], 0)

        return max(case1, case2)