class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        
        n = len(nums)
        res = []
        l = 0 

        for r in range(k - 1, n):

            window = nums[l : r + 1]
            res.append(max(window))
            l += 1

        return res



        