class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        n = len(nums)
        i, j = 0, 1
        res = [0] * n

        for l in range(n):
            if nums[l] > 0:
                res[i] = nums[l]
                i += 2
            else:
                res[j] = nums[l]
                j += 2

        return res
        