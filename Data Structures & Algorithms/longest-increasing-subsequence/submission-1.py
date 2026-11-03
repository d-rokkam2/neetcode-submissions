class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)

        cache = {}
        def backtrack(i, j):
            if i == n:
                return 0

            if (i,j) in cache:
                return cache[(i,j)]

            res = backtrack(i+1, j)

            if j == -1 or nums[j] < nums[i]:
                res = max(res, 1 + backtrack(i+1, i))

            cache[(i,j)] = res
            return cache[(i,j)]

        return backtrack(0,-1)

            

            
        
        
        