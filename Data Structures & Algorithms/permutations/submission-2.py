class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ret = []

        def backtrack(i, curr):

            if len(curr) == len(nums):
                ret.append(curr.copy())
                return

            if i >= len(nums):
                return 

            for n in nums:
                if n not in curr:
                    curr.append(n)
                    backtrack(i + 1, curr)
                    curr.pop()

        backtrack(0, [])
        return ret

