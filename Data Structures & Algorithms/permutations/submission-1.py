class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ret = []
        n = len(nums)
        used = [False] * n

        def backtrack(stack, u):

            if len(stack) == n:
                ret.append(stack.copy())
                return 

            for i in range(n):
                if not u[i]:
                    u[i] = True
                    stack.append(nums[i])
                    backtrack(stack, u)
                    stack.pop()
                    u[i] = False

        backtrack([],used)
        return ret

        