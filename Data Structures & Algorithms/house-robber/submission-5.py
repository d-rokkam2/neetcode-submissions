class Solution:
    def rob(self, nums: List[int]) -> int:

        curr, nexx = 0, 0

        for num in nums:
            temp = max(num + curr, nexx)
            curr = nexx
            nexx = temp

        return nexx

        
