class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        ret = []
        n = len(nums)

        def backtrack(i, curr, total):
            
            if i >= n or total > target:
                return 

            if total == target:
                ret.append(curr.copy())
                return 

            curr.append(nums[i])
            backtrack(i, curr, total + nums[i])
            curr.pop()
            backtrack(i + 1, curr, total)

        backtrack(0, [], 0)
        return ret

            
