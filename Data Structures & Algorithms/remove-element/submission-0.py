class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        k = 0
        n = len(nums)
        for r in range(n):
            if nums[r] != val:
                nums[k] = nums[r]
                k += 1

        return k

            

        