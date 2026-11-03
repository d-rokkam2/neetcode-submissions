class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        currSub, maxSub = 0, nums[0]

        for n in nums:

            if currSub < 0:
                currSub = 0

            currSub += n
            maxSub = max(maxSub, currSub)


        return maxSub


            