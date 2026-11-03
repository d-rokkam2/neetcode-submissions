class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ret, stack = [], []
        n = len(nums)

        
        def backtrack(i):

            if i == n:
                ret.append(stack.copy())
                return

            stack.append(nums[i])
            backtrack(i + 1)
            stack.pop()
            backtrack(i + 1)
            
        backtrack(0)
        return ret
        