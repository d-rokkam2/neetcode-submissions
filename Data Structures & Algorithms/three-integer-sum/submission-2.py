class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        n = len(nums)
        ret = set()

        for i in range(len(nums)):

            curr = nums[i]
            left, right = i + 1, n - 1

            while left < right:

                total = curr + nums[left] + nums[right]
                if  total == 0:
                    ret.add((nums[left], curr, nums[right]))
                    left += 1
                    right -= 1
                elif total > 0:
                    right -= 1
                else:
                    left += 1

        return list(ret)




        