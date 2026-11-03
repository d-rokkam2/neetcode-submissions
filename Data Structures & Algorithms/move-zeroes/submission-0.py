class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        lastPosition = 0
        n = len(nums)
        for current in range(n):
            if nums[current] != 0:
                nums[lastPosition], nums[current] = nums[current], nums[lastPosition]
                lastPosition += 1

                

        