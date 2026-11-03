class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numset = set(nums)
        maxx = len(nums)
        res = []
        for i in range(1,maxx + 1):
            if i not in numset:
                res.append(i)

        return res
