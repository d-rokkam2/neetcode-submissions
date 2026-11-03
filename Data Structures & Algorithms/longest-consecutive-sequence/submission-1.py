class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num_set = set(nums)
        ret = 0

        for num in nums:

            if (num - 1) in num_set:
                continue

            streak = 0
            current = num
            while current in num_set:
                streak += 1
                current += 1

            ret = max(streak, ret)

        return ret
