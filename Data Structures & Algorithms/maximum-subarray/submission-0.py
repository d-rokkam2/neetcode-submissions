class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        currSub, maxSub = 0, nums[0]
        n = len(nums)

        for num in nums:
            if currSub < 0:
                currSub = 0

            currSub += num

            maxSub = max(maxSub, currSub)

        return maxSub




        