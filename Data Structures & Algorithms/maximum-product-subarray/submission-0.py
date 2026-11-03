class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        result = nums[0]
        currMin = 1
        currMax = 1

        for num in nums:

            temp = currMax * num
            currMax = max(temp, num * currMin, num)
            currMin = min(temp, num, num * currMin)

            result = max(result, currMax)

        return result


        