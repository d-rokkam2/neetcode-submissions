class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        n = len(nums)
        res = set()

        for i in range(n):
            l, r = i + 1, n - 1
            while l < r:
                curr = nums[i] + nums[r] + nums[l]
                if curr > 0:
                    r -= 1
                elif curr < 0:
                    l += 1
                else:
                    res.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -=1

        return list(res)

        