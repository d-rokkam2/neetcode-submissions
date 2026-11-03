class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        res = 0
        
        for n in nums:
            if (n - 1) in nums:
                continue
            curr = 1
            while (n + curr) in nums:
                curr += 1

            res = max(res, curr)

        return res

            

            

        
            
        