class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        cache = {}
        n = len(nums)

        def dfs(i):

            if i == len(nums) - 1:
                return True

            if i in cache:
                return cache[i]
            
            if nums[i] == 0:
                return False

            end = i + nums[i] + 1

            for j in range(i + 1, end):

                if dfs(j):
                    cache[i] = True
                    return True

            cache[i] = False
            return False

        return dfs(0)


            
            



