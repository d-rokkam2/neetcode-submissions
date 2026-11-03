class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ret = []
        n = len(nums)

        def backtrack(stack):

            if len(stack) == n:
                ret.append(stack.copy())
                return 

            for num in nums:
                if num not in stack:
                    stack.append(num)
                    backtrack(stack)
                    stack.pop()

        backtrack([])
        return ret

        