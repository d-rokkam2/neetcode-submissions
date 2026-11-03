class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        ret = [1] * n
        prefix = 1

        for i in range(n):
            ret[i] = prefix
            prefix *= nums[i]

        postfix = 1

        for j in range(n-1, -1, -1):
            ret[j] *= postfix
            postfix *= nums[j]

        return ret


        