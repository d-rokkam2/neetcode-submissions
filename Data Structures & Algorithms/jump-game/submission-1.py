class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)
        cache = {}

        def dfs(i):
            
            if i == n -1:
                return True

            if i in cache:
                return cache[i]

            if nums[i] == 0:
                return False

            end = i + nums[i] + 1
            for jum in range(i +1, end):
                if dfs(jum):
                    cache[i] = True 
                    return cache[i]

            cache[i] = False
            return cache[i]

        return dfs(0)

                


            


                

            
        