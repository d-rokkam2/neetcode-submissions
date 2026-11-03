class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        from functools import lru_cache

        n = len(nums)
        res = 1

        @lru_cache(None)
        def backtrack(i, j):
            if i == n:
                return 0

            res = backtrack(i+1, j)

            if j == -1 or nums[j] < nums[i]:
                res = max(res, 1 + backtrack(i+1, i))

            return res

        return backtrack(0,-1)

            

            
        
        
        