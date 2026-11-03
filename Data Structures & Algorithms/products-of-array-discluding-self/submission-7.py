class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = 1
        n = len(nums)
        res = [1] * n

        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for j in range(n -1, -1, -1):
            res[j] *= postfix
            postfix *= nums[j]

        return res


