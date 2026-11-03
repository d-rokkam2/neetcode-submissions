class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        nums.sort()
        ret = set()


        for i in range(n):
            target = nums[i]
            left = i + 1
            right = n - 1

            while left < right:

                if nums[left] + nums[right] + target == 0:
                    ret.add((nums[left], nums[right], target))
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] + target > 0:
                    right -= 1
                else:
                    left += 1

        return list(ret)
                    


        