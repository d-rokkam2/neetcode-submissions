from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        ret = set()
        nums.sort()
        n = len(nums)
        
        

        for i in range(n):
            l, r = i + 1, n - 1
            current = nums[i]
            while l < r:
                total = current + nums[l] + nums[r]
                if total == 0:
                    ret.add((nums[l],current,nums[r]))
                    l += 1
                    r -= 1
                elif total > 0:
                    r -= 1
                else:
                    l += 1

        return list(ret)
                    




        
        