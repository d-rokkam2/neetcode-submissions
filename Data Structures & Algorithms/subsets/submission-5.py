class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        n = len(nums)

        def backtrack(i, curr):
            if i >= n:
                res.append(curr.copy())
                return 

            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr.pop()
            backtrack(i + 1, curr)

        backtrack(0, [])
        return res

        