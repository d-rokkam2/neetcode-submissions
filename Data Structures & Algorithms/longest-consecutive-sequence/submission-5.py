class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        res = 0
        num_set = set(nums)

        for num in num_set:
            if (num - 1) in num_set:
                continue
            curr = 1
            while (num + curr) in num_set:
                curr += 1

            res = max(curr, res)

        return res

        
        
            

            

        
            
        