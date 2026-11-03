class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        n = len(nums)

        def backtrack(i, curr, total):
            # base case
            if total == target:
                res.append(curr.copy())
                return

            if total > target or i >= n:
                return 

            curr.append(nums[i])
            backtrack(i, curr, total + nums[i])
            curr.pop()
            backtrack(i + 1, curr, total)

        backtrack(0, [], 0)
        return res




        