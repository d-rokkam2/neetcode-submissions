class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numset = set(nums)
        ret = 0

        for n in nums:

            if (n-1) in numset:
                continue
            curr = 1

            while (n + curr) in numset:
                curr += 1

            ret = max(curr, ret)


        return ret

            
        