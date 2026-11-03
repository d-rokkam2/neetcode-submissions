class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        ret = []
        for j in range(len(nums)):
            current = 1
            for i in range(len(nums)):
                if j == i:
                    continue
                else:
                    current *= nums[i]

            ret.append(current)
        
        return ret