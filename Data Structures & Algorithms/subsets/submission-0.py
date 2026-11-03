class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ret = []
        n = len(nums)

        
        def backtrack(i, stack):

            if i == n:
                ret.append(stack.copy())
                return

            stack.append(nums[i])
            backtrack(i + 1, stack)
            stack.pop()
            backtrack(i + 1, stack)
            
        backtrack(0, [])
        return ret
        