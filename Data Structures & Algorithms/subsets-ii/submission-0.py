class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        ret = set()
        def backtrack(i, curr):
            if i == n:
                ret.add(tuple(curr.copy()))
                return

            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr.pop()
            backtrack(i + 1, curr)

        nums.sort()
        backtrack(0, [])
        return [list(val) for val in ret]



        